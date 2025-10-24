"""
Paquet principale, contenant les modules métier, calculant les différentes données du plan de nutrition d'une personne.

Structure du paquet :
plan_nutrition/
│
├── __init__.py
├── plan_nutrition.py (classe PlanNutrition)
├── personne/
│   ├── __init__.py
│   ├── personne.py (Classe Personne)
│   ├── activite.py (Classe Activité)
│   └── _attributs.py   (enums utilisées dans les classes Personne et Activité)
├──
└──

"""

from .plan_nutrition import Activité, Personne, PlanNutrition

__all__ = ["PlanNutrition", "Personne", "Activité"]
