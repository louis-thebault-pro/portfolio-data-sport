"""
Module définissant la classe Personne.

Les attributs de la classe sont définis par :
- l'ensemble des données physiologiques (nom, age, sexe, poids, taille, génétique, température corporelle)
- le régime alimentaire de la personne
- l'objectif alimentaire de la personne

Les méthodes de la classe sont :
- get(attribut) prenant en entrée le nom de l'attribut et en sortie la valeur de celui-ci

"""

from ._attributs import Génétique, ObjectifAlimentaire, RégimeAlimentaire, Sexe


class Personne:

    def __init__(
        self,
        nom: str,
        age: int,
        poids: int,
        taille: int,
        sexe: Sexe = Sexe.NON_RENSEIGNE,
        genetique: Génétique = Génétique.NORMALE,
        temperature: int = 37,
        regime_alimentaire: RégimeAlimentaire = RégimeAlimentaire.OMNIVORE,
        objectif_alimentaire: ObjectifAlimentaire = ObjectifAlimentaire.MAINTIEN,
    ):
        self._nom, self._age, self._poids, self._taille = nom, age, poids, taille
        self._sexe, self._genetique, self._temperature = sexe, genetique, temperature
        self._regime, self._objectif, self.activites = (
            regime_alimentaire,
            objectif_alimentaire,
        )

    def get(self, attribut):
        match attribut:
            case "nom":
                return self._nom
            case "age":
                return self._age
            case "poids":
                return self._poids
            case "taille":
                return self._taille
            case "sexe":
                return self._sexe
            case "genetique":
                return self._genetique
            case "temperature":
                return self._temperature
            case "regime_alimentaire":
                return self._regime
            case "objectif_alimentaire":
                return self._objectif
            case _:
                return "Attribut non défini"

    def metabolisme_base(self):
        return (
            10 * self._poids
            + 6.25 * self._taille
            - 5 * self._age
            + {
                (
                    -161
                    if self._sexe == Sexe.FEMME
                    else (5 if self._sexe == Sexe.HOMME else (-161 + 5) / 2)
                )
            }
        )
