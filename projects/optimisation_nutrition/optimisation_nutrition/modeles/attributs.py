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
    FEMME = "Femme"
    HOMME = "Homme"
    NON_RENSEIGNE = "Non renseigné"


class Genetique(StrEnum):
    NORMALE = "Normale"
    RAPIDE = "Rapide"
    LENTE = "Lente"


class RegimeAlimentaire(StrEnum):
    OMNIVORE = "Omnivore"
    PESCO_VEGETARIEN = "Pesco-végétarien"
    VEGETARIEN = "Végétarien"
    VEGETALIEN = "Végétalien"


class ObjectifAlimentaire(StrEnum):
    MAINTIEN = "Maintien du poids"
    PRISE_MASSE = "Prise de masse"
    PERTE_POIDS = "Perte de poids"


class TypeActivite(StrEnum):
    ENDURANCE = "Endurance"
    FORCE = "Force"
    INTERMITTENT = "Intermittent"
    COMBAT = "Combat"
    AGILITE = "Agilité"
    AUTRE = "Autre"
