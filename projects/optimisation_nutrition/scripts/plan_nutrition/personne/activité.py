"""
Module définissant la classe Activité.

Les attributs de cette classe sont :
- son nom (description explicite de l'activité)
- le type d'activité (endurance, force, etc.)
- la durée hebdomadaire de l'activité en heure
- le MET lié à l'activité

Les méthodes liées à la classe sont :
- get(attribut) prenant en entrée le nom de l'attribut et en sortie la valeur de celui-ci
- depense() calculant la dépense brute de l'activité, sans prendre en compte le poids

"""

from .attributs import TypeActivité


class Activité:

    def __init__(self, nom: str, type_activite: TypeActivité, duree: int, met: float):
        self._nom = nom
        self._type_activite = type_activite
        self._duree = duree
        self._met = met

    def get(self, attribut):
        match attribut:
            case "nom":
                return self._nom
            case "type_activité":
                return self._type_activite
            case "duree":
                return self._duree
            case "MET":
                return self._met
            case _:
                return "Attribut non défini"

    def depense(self):
        return self._duree * self._met
