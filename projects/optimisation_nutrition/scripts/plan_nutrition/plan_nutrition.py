"""
Module définissant la classe PlanNutrition.

Les attributs de cette classe sont :
- une personne
- les activités hebdomadaires de la personne sous forme d'une liste d'activités

Les méthodes liées à la classe sont :
- calcul_depense() qui permet de calculer la dépense hebdomadaire d'une personne

"""

from personne import Activité, Personne


class PlanNutrition:

    def __init__(self, personne: Personne, activites: list = []):
        self._personne = personne
        self._activites = []

    def calcul_depenses(self):
        depense = self._personne.metabolisme_base()
        if self._activites == []:
            return depense
        else:
            for activite in self.activites:
                if isinstance(activite, Activité):
                    depense += activite.depense() * self._personne.get("poids")
                else:
                    print(f"{activite} n'est pas une activité")
        return depense
