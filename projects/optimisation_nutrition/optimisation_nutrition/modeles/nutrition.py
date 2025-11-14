"""
Module définissant la classe PlanNutrition.

Attributs de la classe :
- personne --> type Personne
- activités hebdomadaires --> liste d'activités, chacunes du type Activité

Méthodes de la classe :
- __init__() --> initialisation de la classe
- calcul_depense() --> calcul de la dépense énergétique hebdomadaire

"""

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from ..donnees import lire_json
from .activite import Activite
from .personne import Personne


def max_dico(dico: dict):
    """Méthode utile pour les différentes méthodes de la classe Nutrition"""
    valeur_max = 0
    cle_max = ""
    for cle in dico:
        if dico[cle] >= valeur_max:
            valeur_max = dico[cle]
            cle_max = cle
    return cle_max


class Nutrition(BaseModel):
    personne: Personne = Field(
        default=Personne(),
        description="Personne définie grâce à la classe Personne (Par défaut : Marie Martin, française moyenne)",
    )
    activites: list = Field(
        default=[],
        description="Liste d'activités où chacune est définie selon la classe Activité (Par défaut : [])",
    )
    _besoin_hebdo: int = PrivateAttr(default=0)
    _recommandations: dict = PrivateAttr(
        default=lire_json("optimisation_nutrition/donnees/recommandations.JSON")
    )

    model_config = ConfigDict(**{"use_enum_values": True, "validate_assignment": True})

    def metabolisme_base(self):
        return self.personne.metabolisme_base()

    def ajouter_activite(self, activite: Activite):
        self.activites.append(activite)

    def besoins_hebdomadaires(self):
        if self._besoin_hebdo == 0:
            depense = self.metabolisme_base() * 7
            if self.activites == []:
                return depense
            else:
                for activite in self.activites:
                    if isinstance(activite, Activite):
                        depense += activite.calcul_depense() * self.personne.poids
                    else:
                        print(f"{activite} n'est pas une activité")
            self._besoin_hebdo = int(depense)
        return self._besoin_hebdo

    def besoins_quotidiens(self):
        return int(
            self._besoin_hebdo / 7
            if self._besoin_hebdo != 0
            else self.besoins_hebdomadaires() / 7
        )

    def __str__(self):
        return f"{self.personne.prenom} {self.personne.nom}\n Métabolisme de base au quotidien : {self.personne.metabolisme_base()} kcal\n Besoins globaux quotidien : {self.besoins_quotidiens()} kcal"

    def types_activites(self):
        types = {}
        if self.activites != []:
            for activite in self.activites:
                type = activite.type
                if hasattr(type, "value"):
                    cle = str(type.value).strip().lower()
                else:
                    cle = str(type).strip().lower()
                types[cle] = types.get(cle, 0) + 1
            return types
        else:
            return None

    def recommandations_personne(self):
        types = self.types_activites()
        if types:
            profil = max_dico(types)
            reco = self._recommandations.get(profil)
            if profil != "endurance" and "endurance" in types:
                reco["macro"]["glucides"] = self._recommandations["endurance"]["macro"][
                    "glucides"
                ]
            if profil != "force" and "force" in types:
                reco["macro"]["proteines"] = self._recommandations["force"]["macro"][
                    "proteines"
                ]
            elif profil != "combat" and "combat" in types:
                reco["macro"]["proteines"] = self._recommandations["combat"]["macro"][
                    "proteines"
                ]
            return reco
        return None
