"""
Module définissant la classe PlanNutrition.

Attributs de la classe :
- personne --> type Personne
- activités hebdomadaires --> liste d'activités, chacunes du type Activité

Méthodes de la classe :
- __init__() --> initialisation de la classe
- calcul_depense() --> calcul de la dépense énergétique hebdomadaire

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
