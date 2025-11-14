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


def glucides(reco: dict, type: str, intensite: str = None):
    glu = {}
    print(f"glucides : {type}")
    glu["pourcentage"] = reco[type]["macro"]["glucides"]["pourcentage"]
    absolu = reco[type]["macro"]["glucides"]["absolu"]
    if intensite:
        niveau_int = reco[type]["macro"]["glucides"]["intensite"][intensite]
        absolu["min"] += niveau_int
        absolu["max"] += niveau_int
    glu["absolu"] = absolu
    return glu


def proteines(reco: dict, type: str, intensite: str = None, objectif: str = None):
    prot = {}
    print(f"proteines : {type}")
    prot["pourcentage"] = reco[type]["macro"]["proteines"]["pourcentage"]
    absolu = reco[type]["macro"]["proteines"]["absolu"]
    if objectif:
        if objectif == "maintien" and intensite:
            niveau_int = reco[type]["macro"]["proteines"]["intensite"][intensite]
            absolu["min"] += niveau_int
            absolu["max"] += niveau_int
        else:
            niveau_obj = reco[type]["macro"]["proteines"]["poids"][objectif]
            absolu["min"] += niveau_obj
            absolu["max"] += niveau_obj
    prot["absolu"] = absolu
    return prot


def lipides(reco: dict, type: str, objectif: str = None):
    lip = {}
    print(f"lipides : {type}")
    lip["absolu"] = reco[type]["macro"]["lipides"]["absolu"]
    lip["composition"] = reco[type]["macro"]["lipides"]["composition"]
    pourcentage = reco[type]["macro"]["lipides"]["pourcentage"]
    if objectif:
        if objectif == "perte de poids":
            pourcentage["min"] -= 10
            pourcentage["max"] -= 10
    lip["pourcentage"] = pourcentage
    return lip


def fibres(reco: dict, type: str):
    print(f"fibres : {type}")
    return reco[type]["macro"]["fibres"]
