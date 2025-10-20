# -*- coding: utf-8 -*-
"""
Module définissant la classe Activités pour représenter l'ensemble des activités d'un·e athlète.
"""

from pandas import DataFrame
from datetime import datetime


class Activités:
    """Répertoire regroupant un ensemble d'activités sous forme de tableaux de données.

    Attributs :
        activités (dictionnaire) : Activités de l'athlète, avec la date en clé et un DataFrame représentant l'activité en valeur.

    Méthodes :
        __init__ : Initialise l'objet Activités avec les données fournies.
        getActivités : Retourne les activités de l'athlète.
        getActivité : Retourne une activité de l'athlète à une date donnée.
        addActivité : Ajoute une activité à la liste des activités de l'athlète.
        removeActivité : Supprime une activité de la liste des activités de l'athlète.
    """

    def __init__(self, activités: dict[datetime, DataFrame] = {}):
        self._activités = activités

    def getActivités(self) -> dict[datetime, DataFrame]:
        """Retourne les activités de l'athlète."""
        return self._activités

    def getActivité(self, date: datetime) -> DataFrame:
        """Retourne une activité de l'athlète à une date donnée."""
        return self._activités[date]

    def addActivité(self, date: datetime, activité: DataFrame) -> None:
        """Ajoute une activité à la liste des activités de l'athlète."""
        self._activités[date] = activité

    def removeActivité(self, date: datetime) -> None:
        """Supprime une activité de la liste des activités de l'athlète."""
        if date in self._activités:
            del self._activités[date]
