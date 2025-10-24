"""
Paquet annexe au paquet principal contenant les modules décrivant une personne.

Structure du paquet :
personne/
│
├── __init__.py
├── personne.py (Classe Personne)
├── activite.py (Classe Activité)
└── _attributs.py   (enums utilisées dans les classes Personne et Activité)*

"""

from .activité import Activité
from .personne import Personne

__all__ = ["Activité", "Personne"]
