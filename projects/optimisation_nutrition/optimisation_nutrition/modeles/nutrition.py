"""
Module définissant la classe Nutrition

Attributs de la classe :
    - personne --> type Personne
    - activités hebdomadaires --> liste d'activités, chacunes du type Activité

Méthodes de la classe :
    - metabolisme_base()
    - ajouter_activite()
    - besoins_hebdomadaires()
    - besoins_quotidiens()
    - types_activites()
    - recommandations_personne()

"""

from numpy import mean
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from ..donnees import lire_json
from .activite import Activite
from .personne import Personne
from .utils import fibres, glucides, lipides, max_dico, proteines


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

    def __str__(self):
        return f"{self.personne.prenom} {self.personne.nom}\n Métabolisme de base au quotidien : {self.personne.metabolisme_base()} kcal\n Besoins globaux quotidien : {self.besoins_quotidiens()} kcal"

    def besoins_quotidiens_hors_sport(self):
        return self.personne.besoins_quotidiens()

    def ajouter_activite(self, activite: Activite):
        self.activites.append(activite)

    def besoins_hebdomadaires(self):
        if self._besoin_hebdo == 0:
            depense = self.besoins_quotidiens_hors_sport() * 7
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

    def types_activites(self):
        types, poids_types, intensite = {}, {}, {}
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
                intensite[cle] = (
                    "forte" if int >= 2.5 else ("moyenne" if int >= 1.5 else "faible")
                )

            total = sum(types.values())
            poids_types = (
                {k: 0 for k in types}
                if total == 0
                else {cle: valeur / total for cle, valeur in types.items()}
            )
            return types, poids_types, intensite
        else:
            return None, None

    def recommandations_personne(self):

        types, poids_types, intensite = self.types_activites()
        objectif = self.personne.objectif

        if not types:
            return None

        macro = {}
        type_principal = max_dico(types)

        macro["glucides"] = glucides(
            reco=self._recommandations,
            poids_types=poids_types,
            intensite=intensite,
        )
        macro["proteines"] = proteines(
            reco=self._recommandations,
            poids_types=poids_types,
            intensite=intensite,
            objectif=objectif,
        )
        macro["lipides"] = lipides(
            reco=self._recommandations, type=type_principal, objectif=objectif
        )
        macro["fibres"] = fibres(reco=self._recommandations, type=type_principal)
        reco = {}
        reco["macro"] = macro
        return reco

    def plan_nutrition(self):
        reco = self.recommandations_personne()
        poids = self.personne.poids
        besoins_quot = self.besoins_quotidiens()

        print("Besoins quotidiens (kcal) :", besoins_quot)

        if not reco:
            return None

        glu_abs = [
            poids * reco["macro"]["glucides"]["absolu"]["min"],
            poids * reco["macro"]["glucides"]["absolu"]["max"],
        ]
        prot_abs = [
            poids * reco["macro"]["proteines"]["absolu"]["min"],
            poids * reco["macro"]["proteines"]["absolu"]["max"],
        ]
        lip_abs = [
            poids * reco["macro"]["lipides"]["absolu"]["min"],
            poids * reco["macro"]["lipides"]["absolu"]["max"],
        ]
        fib_abs = reco["macro"]["fibres"]["absolu"]["max"]

        glu_pourc_reel = [
            int(100 * glu_abs[0] * 4 / besoins_quot),
            int(100 * glu_abs[1] * 4 / besoins_quot),
        ]
        prot_pourc_reel = [
            int(100 * prot_abs[0] * 4 / besoins_quot),
            int(100 * prot_abs[1] * 4 / besoins_quot),
        ]
        lip_pourc_reel = [
            int(100 * lip_abs[0] * 9 / besoins_quot),
            int(100 * lip_abs[1] * 9 / besoins_quot),
        ]

        glu_pourc_reco = [
            reco["macro"]["glucides"]["pourcentage"]["min"],
            reco["macro"]["glucides"]["pourcentage"]["max"],
        ]
        prot_pourc_reco = [
            reco["macro"]["proteines"]["pourcentage"]["min"],
            reco["macro"]["proteines"]["pourcentage"]["max"],
        ]
        lip_pourc_reco = [
            reco["macro"]["lipides"]["pourcentage"]["min"],
            reco["macro"]["lipides"]["pourcentage"]["max"],
        ]

        besoins = {
            "glucides": {
                "absolu": float(mean(glu_abs)),
                "pourcentage_reel": int(mean(glu_pourc_reel)),
                "pourcentage_recommande": int(mean(glu_pourc_reco)),
            },
            "proteines": {
                "absolu": float(mean(prot_abs)),
                "pourcentage_reel": int(mean(prot_pourc_reel)),
                "pourcentage_recommande": int(mean(prot_pourc_reco)),
            },
            "lipides": {
                "absolu": float(mean(lip_abs)),
                "pourcentage_reel": int(mean(lip_pourc_reel)),
                "pourcentage_recommande": int(mean(lip_pourc_reco)),
            },
            "fibres": {"absolu": fib_abs},
        }
        return besoins
