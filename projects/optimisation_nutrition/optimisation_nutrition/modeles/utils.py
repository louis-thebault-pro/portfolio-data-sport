# -*- coding: utf-8 -*-
"""
Module regroupant des fonctions utiles aux différentes classes, modèles et interfaces utilisateur.

Fonctions permettant de normaliser les chaînes relatives aux différents attributs Enum :
    - normaliser_str(entree)
    - conversion_enum(entree, enum)
    - valeurs_enum(enum)
    Grâce à ces fonctions, le projet accepte les entrées quelque soit la casse.

Fonctions utiles à la construction des recommandations nutritives dans la classe Nutrition :
    - glucides(recommandations_de_base, type, intensite)
    - proteines(recommandations_de_base, type, intensite, objectif)
    - lipides(recommandations_de_base, type, objectif)
    - fibres(recommandations_de_base, type)
"""

from enum import Enum

# Fonctions pour la normalisation des Enums


def normaliser_str(entree):
    """Normalise l'élément entré en une chaîne de caractère, en minuscule, ou None si l'entrée est None"""
    return None if entree is None else str(entree).strip().lower()


def conversion_enum(entree, enum: Enum):
    """
    Fonction tentant de convertir une donnée entrée en un membre de l'énumération  enum.
    La valeur retournée est le membre Enum ou None
    Si la conversion échoue, une erreur est levée.
    """
    if isinstance(entree, enum):
        # Si c'est déjà une instance d'enum, entree est renvoyé
        return entree
    if entree is None:
        # Si l'entrée est None, on renvoie None
        return None
    e = normaliser_str(entree)  # Normalisation de l'entrée
    for member in enum:
        if normaliser_str(member.value) == e or normaliser_str(member.name) == e:
            # Si l'entrée normalisée est reconnue parmi les membres de l'enum, on renvoie ce membre
            return member
    # Si aucun des tests ci-dessus n'a fonctionné, on tente une construction directe
    try:
        return enum(entree)
    except Exception as exc:
        # Si ça ne fonctionne pas, on lève une erreur
        raise ValueError(f"Cannot parse {entree!r} as {enum}") from exc


def valeurs_enum(enum: Enum):
    """Retourne la liste des valeurs d'une classe Enum"""
    return [e.value for e in enum]


# Fonctions pour la classe Nutrition


def max_dico(dico: dict):
    """Fonction permettant de trouver la valeur maximale dans un dict"""
    valeur_max = 0
    cle_max = ""
    for cle in dico:
        if isinstance(dico[cle], int) or isinstance(dico[cle], float):
            if dico[cle] >= valeur_max:
                valeur_max = dico[cle]
                cle_max = cle
    return cle_max


def ponderation_macro_par_type(
    reco: dict,
    poids_types: dict,
    relativite: str,
    macro_par_type,
    intensite: dict,
    objectif: str = None,
):
    """
    Pondère min/max sur tous les types détectés selon leurs poids.
    macro_par_type : fonction glucides_par_type ou proteines_par_type
    """
    absolu = {"min": 0, "max": 0}

    for type, poids in poids_types.items():

        valeurs = macro_par_type(
            reco=reco,
            type=type,
            relativite=relativite,
            intensite=(intensite[type] if type in intensite else None),
            objectif=objectif,
        )

        absolu["min"] += valeurs["min"] * poids
        absolu["max"] += valeurs["max"] * poids

    absolu["min"] = (
        round(absolu["min"], 1) if relativite == "absolu" else int(absolu["min"])
    )
    absolu["max"] = (
        round(absolu["max"], 1) if relativite == "absolu" else int(absolu["max"])
    )
    return absolu


def glucides_par_type(
    reco: dict, type: str, relativite: str, intensite: str = None, objectif: str = None
):
    """
    Renvoie uniquement les valeurs absolues min/max ajustées par intensité
    pour un type donné (endurance / force / combat / autre)
    """
    absolu = reco[type]["macro"]["glucides"][relativite].copy()

    if intensite:
        if "intensite" in reco[type]["macro"]["glucides"]:
            niveau_int = reco[type]["macro"]["glucides"]["intensite"][intensite]
            absolu["min"] += niveau_int
            absolu["max"] += niveau_int

    return absolu


def glucides(reco: dict, poids_types: dict, intensite: dict):
    glu = {}
    glu["pourcentage"] = ponderation_macro_par_type(
        poids_types=poids_types,
        reco=reco,
        relativite="pourcentage",
        intensite=intensite,
        macro_par_type=glucides_par_type,
    )
    glu["absolu"] = ponderation_macro_par_type(
        poids_types=poids_types,
        reco=reco,
        relativite="absolu",
        intensite=intensite,
        macro_par_type=glucides_par_type,
    )
    return glu


def proteines_par_type(
    reco: dict, type: str, relativite: str, intensite: str = None, objectif: str = None
):
    """
    Renvoie les valeurs absolues min/max ajustées pour intensité + objectif
    pour un type donné
    """
    absolu = reco[type]["macro"]["proteines"][relativite].copy()

    if objectif:
        if objectif == "maintien du poids" and intensite:
            if "intensite" in reco[type]["macro"]["proteines"]:
                niveau_int = reco[type]["macro"]["proteines"]["intensite"][intensite]
                absolu["min"] += niveau_int
                absolu["max"] += niveau_int
        else:
            if "poids" in reco[type]["macro"]["proteines"]:
                niveau_obj = reco[type]["macro"]["proteines"]["poids"][objectif]
                absolu["min"] += niveau_obj
                absolu["max"] += niveau_obj

    return absolu


def proteines(
    reco: dict,
    poids_types: dict,
    intensite: dict,
    objectif: str = None,
):
    prot = {}
    prot["pourcentage"] = ponderation_macro_par_type(
        poids_types=poids_types,
        reco=reco,
        relativite="pourcentage",
        intensite=intensite,
        objectif=objectif,
        macro_par_type=proteines_par_type,
    )
    prot["absolu"] = ponderation_macro_par_type(
        poids_types=poids_types,
        reco=reco,
        relativite="absolu",
        intensite=intensite,
        objectif=objectif,
        macro_par_type=proteines_par_type,
    )
    return prot


def lipides(reco: dict, type: str, objectif: str = None):
    lip = {}
    lip["absolu"] = reco[type]["macro"]["lipides"]["absolu"].copy()
    lip["composition"] = reco[type]["macro"]["lipides"]["composition"].copy()
    pourcentage = reco[type]["macro"]["lipides"]["pourcentage"].copy()
    if objectif:
        if objectif == "perte de poids":
            pourcentage["min"] -= 10
            pourcentage["max"] -= 10
    lip["pourcentage"] = pourcentage
    return lip


def fibres(reco: dict, type: str):
    return reco[type]["macro"]["fibres"].copy()
