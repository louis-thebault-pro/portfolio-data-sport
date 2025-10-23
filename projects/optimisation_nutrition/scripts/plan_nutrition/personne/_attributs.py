"""
Module permettant de définir certains attributs utilisés dans les classes Activité et Personne

"""

from enum import StrInt


class Sexe(StrInt):
    HOMME = 0
    FEMME = 1
    NON_RENSEIGNE = 2


class Génétique(StrInt):
    NORMALE = 0
    RAPIDE = 1
    LENTE = -1


class RégimeAlimentaire(StrInt):
    OMNIVORE = 0
    PESCO_VEGETARIEN = 1
    VEGETARIEN = 2
    VEGETALIEN = 3


class ObjectifAlimentaire(StrInt):
    MAINTIEN = 0
    PRISE_MASSE = 1
    PERTE_POIDS = -1


class TypeActivité(StrInt):
    ENDURANCE = 0
    FORCE = 1
    INTERMITTENT = 2
    COMBAT = 3
    AGILITE = 4
    AUTRE = 5
