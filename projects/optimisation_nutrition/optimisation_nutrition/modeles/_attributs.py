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
    HOMME = "homme"
    FEMME = "femme"
    NON_RENSEIGNE = "non renseigné"


class Genetique(StrEnum):
    NORMALE = "normale"
    RAPIDE = "rapide"
    LENTE = "lente"


class RegimeAlimentaire(StrEnum):
    OMNIVORE = "omnivore"
    PESCO_VEGETARIEN = "pesco-végétarien"
    VEGETARIEN = "végétarien"
    VEGETALIEN = "végétalien"


class ObjectifAlimentaire(StrEnum):
    MAINTIEN = "maintien"
    PRISE_MASSE = "prise de masse"
    PERTE_POIDS = "perte de poids"


class TypeActivite(StrEnum):
    ENDURANCE = "endurance"
    FORCE = "force"
    INTERMITTENT = "intermittent"
    COMBAT = "combat"
    AGILITE = "agilité"
    AUTRE = "autre"
