"""
Module définissant la classe PlanNutrition.

Attributs de la classe :
- personne --> type Personne
- activités hebdomadaires --> liste d'activités, chacunes du type Activité

Méthodes de la classe :
- __init__() --> initialisation de la classe
- calcul_depense() --> calcul de la dépense énergétique hebdomadaire

"""

from pydantic import BaseModel, Field

from .activite import Activite
from .personne import Personne


class Nutrition(BaseModel):
    personne: Personne = Field(
        default=Personne(),
        description="Personne définie grâce à la classe Personne (Par défaut : Marie Martin, française moyenne)",
    )
    activites: list = Field(
        default=[],
        description="Liste d'activités où chacune est définie selon la classe Activité (Par défaut : [])",
    )
    besoin_hebdo: int = 0

    class ConfigDict:
        use_enum_values = True
        validate_assignment = True

    def metabolisme_base(self):
        return self.personne.metabolisme_base()

    def ajouter_activite(self, activite: Activite):
        self.activites.append(activite)

    def besoins_hebdomadaires(self):
        if self.besoin_hebdo == 0:
            depense = self.metabolisme_base() * 7
            if self.activites == []:
                return depense
            else:
                for activite in self.activites:
                    if isinstance(activite, Activite):
                        depense += activite.calcul_depense() * self.personne.poids
                    else:
                        print(f"{activite} n'est pas une activité")
            self.besoin_hebdo = depense
            return int(depense)
        else:
            return self.besoin_hebdo

    def besoins_quotidiens(self):
        return int(
            self.besoin_hebdo / 7
            if self.besoin_hebdo != 0
            else self.besoins_hebdomadaires() / 7
        )

    def __str__(self):
        return f"{self.personne.prenom} {self.personne.nom}\n Métabolisme de base au quotidien : {self.personne.metabolisme_base()} kcal\n Besoins globaux quotidien : {self.besoins_quotidiens()} kcal"
