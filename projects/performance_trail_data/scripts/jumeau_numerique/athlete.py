# -*- coding: utf-8 -*-
"""
Module définissant la classe Athlete pour représenter un·e athlète, sa pysiologie et ses activités.
"""

from datetime import date
from .activités import Activités, DataFrame


class Athlete:
    """Représentation d'un·e athlète (données personnelles et physiologie), en répertoriant ses activités.

    Attributs :
        infos (dictionnaire) : Données principales décrivant l'athlète (Nom, âge, sexe, etc.).
        physio (dictionnaire) : Données physiologiques de l'athlète (VMA, VO2, etc.).
        activités (dictionnaire) : Activités de l'athlète, avec la date en clé et un DataFrame décrivant l'activité en valeur.

    Méthodes :
        __init__ : Initialise un objet Athlete avec les données fournies.
        __str__ : Retourne une représentation textuelle de l'athlète.
        getInfos, getPhysio, getActivités : Retourne les différents attributs de l'athlète.
        setData : Modifie une donnée (descriptive ou physiologique) de l'athlète.
        addActivité, removeActivité : Ajoute ou supprime une activité de l'athlète.
    """

    def __init__(
        self,
        nom: str,
        prenom: str,
        naissance: date,
        poids: float,
        taille: int,
        sexe: str,
        VMA: float,
        VO2max: float,
        FCrepos: int,
        FCmax: int,
        SV1: int,
        SV2: int,
        durabilité: int,
        activités: Activités = Activités(),
    ):
        self._infos = {
            "nom": nom,
            "prenom": prenom,
            "age": (
                date.today().year - naissance.year
                if date.today()
                > date(date.today().year, naissance.month, naissance.day)
                else date.today().year - naissance.year - 1
            ),
            "poids": poids,
            "taille": taille,
            "sexe": (sexe if sexe in ["M", "F"] else "Non renseigné"),
        }
        self._physio = {
            "VMA": VMA,
            "VO2max": VO2max,
            "FCrepos": FCrepos,
            "FCmax": FCmax,
            "SV1": SV1,
            "SV2": SV2,
            "durabilité": durabilité,
        }
        self._activités = activités

    def __str__(self):
        return (
            f'{self._infos["prenom"]} {self._infos["nom"]}'
            f' | {"Homme" if self._infos["sexe"] == "M" else ("Femme" if self._infos["sexe"] == "F" else "Sexe non renseigné")}'
            f' | {self._infos["age"]} ans | {self._infos["poids"]} kg | {self._infos["taille"]} cm'
        )

    def getInfos(self) -> dict:
        """Retourne les informations principales de l'athlète."""
        return self._infos

    def getPhysio(self) -> dict:
        """Retourne les données physiologiques de l'athlète."""
        return self._physio

    def setData(self, nom, valeur) -> None:
        """Modifie une donnée de l'athlète."""
        if nom in self._infos:
            self._infos[nom] = valeur
        elif nom in self._physio:
            self._physio[nom] = valeur
        else:
            raise ValueError(
                f"La donnée '{nom}' n'existe pas dans les informations ou les données physiologiques de l'athlète."
            )

    def getActivités(self) -> dict[date, DataFrame]:
        """Retourne les activités de l'athlète."""
        return self._activités.getActivités()

    def addActivité(self, date: date, activité) -> None:
        """Ajoute une activité à la liste des activités de l'athlète."""
        self._activités.addActivité(date, activité)

    def removeActivité(self, date: date) -> None:
        """Supprime une activité de la liste des activités de l'athlète."""
        self._activités.removeActivité(date)
