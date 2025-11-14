"""
Module regroupant des fonctions permettant la normalisation des chaînes de caractères et l'analyse des énumérations dans le projet.
Il regroupe des fonctions utilisées par les modèles Pydantic et l'interface utilisateur Streamlit.
Grâce à ces fonctions, le projet accepte les entrées quelque soit la casse.

Fonctions :
- normaliser_str(entree)
- conversion_enum(entree, enum)
- valeurs_enum(enum)
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
