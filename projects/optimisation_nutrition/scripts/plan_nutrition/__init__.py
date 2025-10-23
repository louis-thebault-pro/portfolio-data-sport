"""
Paquet Python contenant les modules calculant le plan de nutrition d'une personne.

Modules du paquet :
- PlanNutrition
- personne
    - Activité
    - Personne

"""

from .plan_nutrition import Activité, Personne, PlanNutrition

__all__ = ["PlanNutrition", "Personne", "Activité"]
