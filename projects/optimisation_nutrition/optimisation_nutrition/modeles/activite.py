# -*- coding: utf-8 -*-
"""
Module définissant la classe Activite.

Attributs de la classe :
    - description : str --> description explicite de l'activité
    - type : TypeActivite --> type de l'activité (endurance, force, etc.)
    - duree : float --> durée hebdomadaire de l'activité en heures
    - met : float --> MET (Metabolic Equivalent Task) associé à l'activité
    - _intensite : Intensite --> attribut privé défini en fonction du temps et du met de l'activité

Méthodes :
    - calcul_depense() --> calcule la dépense énergétique hebdomadaire sans prendre en compte le poids

"""

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from ..donnees import MET
from .attributs import Intensite, TypeActivite
from .utils import conversion_enum


class Activite(BaseModel):
    sport: str = Field(
        default="Marche",
        description="Sport principal lié à l'activité (Défaut : Marche)",
        min_length=3,
    )
    description: str = Field(
        default="Randonnée",
        description="Description de l'activité (Défaut : Randonnée)",
        min_length=3,
    )
    duree: int = Field(
        default=0, gt=0, description="Durée de l'activité à renseigner en minutes (>0)"
    )
    _intensite: Intensite = PrivateAttr(default=None)
    _type: TypeActivite = PrivateAttr(default=TypeActivite.ENDURANCE)
    _met: float = PrivateAttr(default=7)

    model_config = ConfigDict(**{"use_enum_values": True, "validate_assignment": True})

    def model_post_init(self, __context):
        """Méthode appelée automatiquement pour fixer les attributs privés"""

        # Type et MET
        try:
            activite = MET[self.sport][self.description]
            try:
                self._type = conversion_enum(activite["type"], TypeActivite)
            except Exception:
                self._type = TypeActivite.AUTRE
            try:
                self._met = float(activite["met"])
            except Exception:
                self._met = 0
        except Exception:
            self._type = TypeActivite.AUTRE
            self._met = 0

        # Intensité
        depense = self.calcul_depense()
        type_val = (
            self._type.value.strip().lower()
            if hasattr(self._type, "value")
            else str(self._type).strip().lower()
        )
        if type_val in ("endurance", "force"):
            if depense >= 12:
                self._intensite = Intensite.FORTE
            elif depense >= 6:
                self._intensite = Intensite.MOYENNE
            else:
                self._intensite = Intensite.FAIBLE

    @property
    def type(self):
        return self._type

    @property
    def met(self):
        return self._met

    @property
    def intensite(self):
        return self._intensite

    def __str__(self):
        intensite = f" - {self.intensite} intensité" if self.intensite else ""
        return f"{self.sport} : {self.description} ({self._type}) - {self.duree} min - {self._met} METs{intensite}"

    def calcul_depense(self) -> float:
        """
        Calcule la dépense énergétique liée à l'activité sans prendre en compte le poids.
        Formule : dépense = MET * durée
        """
        return self._met * (self.duree / 60)
