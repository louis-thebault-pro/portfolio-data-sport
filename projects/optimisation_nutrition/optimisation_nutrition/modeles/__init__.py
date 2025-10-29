"""
Paquet regroupant les modules permettant de modéliser les différents objets utilisés par le programme (Une personne, ses activités et ses besoins nutritionnels).

Structure du paquet :
modeles/
│
├── __init__.py
├── personne.py (Classe Personne)
├── activite.py (Classe Activité)
├── nutrition.py (Classe Nutrition)
└── _attributs.py   (enums utilisées dans les classes Personne et Activité)*

"""

from .nutrition import Activite, Nutrition, Personne

__all__ = ["Activite", "Personne", "Nutrition"]
