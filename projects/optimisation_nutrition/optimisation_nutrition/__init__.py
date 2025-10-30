"""
Backend du programme, ce paquet contient les modules métier.
Ils permettent de modéliser différents objets utiles au programme comme une personne ou une activité.

Structure du paquet :
optimisation_nutrition/
│
├── __init__.py
├── donnees/
└── modeles/ (paquet regroupant les classes liées à la modélisation des objets utilisés dans le programme comme une personne ou une activité)

"""

from .modeles import (
    Activite,
    Nutrition,
    ObjectifAlimentaire,
    Personne,
    RegimeAlimentaire,
    Sexe,
    TypeActivite,
)

__all__ = [
    "Activite",
    "Personne",
    "Nutrition",
    "Sexe",
    "RegimeAlimentaire",
    "ObjectifAlimentaire",
    "TypeActivite",
]
