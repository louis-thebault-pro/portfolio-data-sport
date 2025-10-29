"""
Backend du programme, ce paquet contient les modules métier.
Ces derniers permettent de modéliser un personne et ses activités, puis ses besoins nutritionnels.

Structure
optimisation_nutrition/
│
├── __init__.py
├── donnees/
├── modeles/
│   ├── __init__.py
│   ├── personne.py (Classe Personne)
│   ├── activite.py (Classe Activité)
│   ├── nutrition.py (classe Nutrition)
│   └── _attributs.py   (enum utilisés pour des attributs des classes Personne et Activité)
└──

"""

from .modeles import Activite, Nutrition, Personne

__all__ = ["Nutrition", "Personne", "Activite"]
