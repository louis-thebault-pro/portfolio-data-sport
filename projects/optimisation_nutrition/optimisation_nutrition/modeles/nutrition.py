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

from optimisation_nutrition.donnees import recommandations

from ..donnees import lire_json
from .activite import Activite
from .personne import Personne
from .utils import fibres, glucides, lipides, proteines


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
        types, intensite = {}, {}
        if self.activites != []:
            for activite in self.activites:
                type = activite.type
                cle = (
                    str(type.value).strip().lower()
                    if hasattr(type, "value")
                    else str(type).strip().lower()
                )
                types[cle] = types.get(cle, 0) + activite.calcul_depense()

                if cle == "endurance" or cle == "force":
                    intensite[cle] = intensite.get(cle, 0) + (
                        activite.calcul_depense()
                        if activite.intensite == "faible"
                        else (
                            2 * activite.calcul_depense()
                            if activite.intensite == "moyenne"
                            else 3 * activite.calcul_depense()
                        )
                    )
            for cle in intensite:
                int = intensite[cle] / types[cle]
                print(int)
                intensite[cle] = (
                    "forte" if int >= 2.5 else ("moyenne" if int >= 1.5 else "faible")
                )

            return types, intensite
        else:
            return None, None

    def recommandations_personne(self):
        types, intensite = self.types_activites()
        objectif = self.personne.objectif
        if types:
            macro = {}
            type_principal = max_dico(types)
            print(f"Type principal : {type_principal}")
            macro["glucides"] = (
                glucides(
                    reco=self._recommandations,
                    type="endurance",
                    intensite=intensite["endurance"],
                )
                if "endurance" in types
                else glucides(reco=self._recommandations, type=type_principal)
            )
            macro["proteines"] = (
                proteines(
                    reco=self._recommandations,
                    type="force",
                    intensite=intensite["force"],
                )
                if "force" in types
                else (
                    proteines(reco=self._recommandations, type="combat")
                    if "combat" in types
                    else proteines(reco=self._recommandations, type=type_principal)
                )
            )
            macro["lipides"] = lipides(
                reco=self._recommandations, type=type_principal, objectif=objectif
            )
            macro["fibres"] = fibres(reco=self._recommandations, type=type_principal)
            reco = {}
            reco["macro"] = macro
            return reco
        return None
