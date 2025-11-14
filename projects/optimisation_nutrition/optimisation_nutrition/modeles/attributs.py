"""
Définition de plusieurs attributs utilisés dans les classes Activité et Personne.

Attributs définis :
- Sexe
- Génétique
- Régime alimentaire
- Objectif alimentaire
- Type d'activité

"""

from enum import StrEnum


class Sexe(StrEnum):
    FEMME = "femme"
    HOMME = "homme"
    NON_RENSEIGNE = "non renseigné"


class RegimeAlimentaire(StrEnum):
    OMNIVORE = "omnivore"
    PESCO_VEGETARIEN = "pesco-végétarien"
    VEGETARIEN = "végétarien"
    VEGETALIEN = "végétalien"


class ObjectifAlimentaire(StrEnum):
    MAINTIEN = "maintien du poids"
    PRISE_MASSE = "prise de masse"
    PERTE_POIDS = "perte de poids"


class TypeActivite(StrEnum):
    SEDENTAIRE = "sédentaire"
    ENDURANCE = "endurance"
    FORCE = "force"
    INTERMITTENT = "intermittent"
    COMBAT = "combat"
    AGILITE = "agilité"
    AUTRE = "autre"


class Intensite(StrEnum):
    FAIBLE = "faible"
    MOYENNE = "moyenne"
    FORTE = "forte"
