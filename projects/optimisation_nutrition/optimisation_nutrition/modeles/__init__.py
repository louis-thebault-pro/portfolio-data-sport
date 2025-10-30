"""
Paquet regroupant les modules modélisant les différents objets utilisés par le programme
(personne, activité et nutrition) et les enums partagées (attributs utiles pour les modèles).

Structure du paquet :
modeles/
├── __init__.py
├── personne.py (Classe Personne)
├── activite.py (Classe Activité)
├── nutrition.py (Classe Nutrition)
└── attributs.py   (enums utilisées dans les classes Personne et Activité)
"""

from .attributs import (
    ObjectifAlimentaire,
    RegimeAlimentaire,
    Sexe,
    TypeActivite,
)
from .nutrition import Activite, Nutrition, Personne

__all__ = [
    "Activite",
    "Personne",
    "Nutrition",
    "Sexe",
    "RegimeAlimentaire",
    "ObjectifAlimentaire",
    "TypeActivite",
]
