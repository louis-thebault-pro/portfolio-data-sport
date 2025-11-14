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

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, field_validator

from .attributs import Intensite, TypeActivite
from .utils import conversion_enum


class Activite(BaseModel):
    description: str = Field(
        default="Activité diverse",
        description="Description de l'activité (Défaut : Activité diverse)",
        min_length=3,
    )
    type: TypeActivite = Field(
        default=TypeActivite.AUTRE,
        description="Type de l'activité à choisir entre endurance, force, etc. (Par défaut : 'autre')",
    )
    duree: int = Field(
        default=0, gt=0, description="Durée de l'activité à renseigner en minutes (>0)"
    )
    met: float = Field(
        default=0,
        gt=0,
        description="Valeur MET de l'activité issue des tables de données (>0)",
    )
    _intensite: Intensite = PrivateAttr(default=None)

    model_config = ConfigDict(**{"use_enum_values": True, "validate_assignment": True})

    @field_validator("type", mode="before")
    def _conversion_type(cls, type):
        return conversion_enum(type, TypeActivite)

    def model_post_init(self, __context):
        """Méthode appelée automatiquement pour fixer l'attribut intensité"""
        depense = self.calcul_depense()
        if self.type == "endurance" or self.type == "force":
            if depense >= 12:
                self._intensite = Intensite.FORTE
            elif depense >= 6:
                self._intensite = Intensite.MOYENNE
            else:
                self._intensite = Intensite.FAIBLE

    @property
    def intensite(self):
        return self._intensite

    def __str__(self):
        intensite = f" - {self.intensite} intensité" if self.intensite else ""
        return f"{self.description} ({self.type}) - {self.duree} min - {self.met} METs{intensite}"

    def calcul_depense(self) -> float:
        """
        Calcule la dépense énergétique liée à l'activité sans prendre en compte le poids.
        Formule : dépense = MET * durée
        """
        return self.met * (self.duree / 60)
