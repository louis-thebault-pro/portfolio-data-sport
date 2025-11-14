"""
Module définissant la classe Personne.

Les attributs de la classe sont définis par :
    - les données physiologiques (prenom, nom, age, sexe, poids, taille)
    - le régime alimentaire de la personne
    - l'objectif alimentaire de la personne

Les méthodes de la classe sont :
    - metabolisme_base()

"""

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, field_validator

from .attributs import ObjectifAlimentaire, RegimeAlimentaire, Sexe
from .utils import conversion_enum


class Personne(BaseModel):
    prenom: str = Field(
        default="Marie",
        description="Prénom de la personne (Par défaut : Marie)",
        min_length=2,
    )
    nom: str = Field(
        default="Martin",
        description="Nom de famille de la personne (Par défaut : Martin)",
        min_length=1,
    )
    age: int = Field(
        default=42,
        description="Âge de la personne (>0) en années (Par défaut : 42 ans)",
        gt=0,
        lt=120,
    )
    sexe: Sexe = Field(
        default=Sexe.FEMME,
        description="Sexe de la personne, défini par une valeur de la classe Sexe, (Par défaut : Femme)",
    )
    poids: float = Field(
        default=68,
        description="Poids de la personne (>0 et <650) en kg (Par défaut : 68 kg)",
        gt=0,
        lt=650,
    )
    taille: int = Field(
        default=163,
        description="Taille de la personne (>0 et <280) en cm (Par défaut : 163 cm)",
        gt=0,
        lt=280,
    )
    regime: RegimeAlimentaire = Field(
        default=RegimeAlimentaire.OMNIVORE,
        description="Régime alimentaire de la personne, defini par la classe RégimeAlimentaire (Par défaut : OMNIVORE)",
    )
    objectif: ObjectifAlimentaire = Field(
        default=ObjectifAlimentaire.MAINTIEN,
        description="Objectif alimentaire de la personne, défini par la classe ObjectifAlimentaire (Par défaut : MAINTIEN)",
    )
    nap: float = Field(
        default=1.4,
        description="NAP - Indice décrivant l'activité de la personne hors sport",
        gt=0,
        lt=2.5,
    )
    _mb: int = PrivateAttr(default=0)

    model_config = ConfigDict(**{"use_enum_values": True, "validate_assignment": True})

    @field_validator("sexe", mode="before")
    def _norm_sexe(cls, v):
        return conversion_enum(v, Sexe)

    @field_validator("regime", mode="before")
    def _norm_regime(cls, v):
        return conversion_enum(v, RegimeAlimentaire)

    @field_validator("objectif", mode="before")
    def _norm_objectif(cls, v):
        return conversion_enum(v, ObjectifAlimentaire)

    def __str__(self):
        # Affiche la valeur lisible du sexe si disponible
        sexe_val = None
        if hasattr(self.sexe, "value"):
            sexe_val = self.sexe.value
        elif isinstance(self.sexe, str):
            sexe_val = self.sexe
        sexe_part = (
            f"{sexe_val}, "
            if sexe_val and sexe_val.strip().lower() != "non renseigné"
            else ""
        )
        return f"{self.prenom} {self.nom}\n {sexe_part}{self.age} ans\n {self.taille/100} m, {self.poids} kg"

    def metabolisme_base(self):
        """
        Calcule la dépense énergétique liée au métabolisme de base, donc l'énergie minimale dont le corps de la personne a besoin pour fonctionner.
        Formule utilisée : Black et al.
        """
        if self._mb == 0:
            terme_sexe = (
                230
                if self.sexe == Sexe.FEMME
                else (259 if self.sexe == Sexe.HOMME else 245)
            )
            self._mb = int(
                terme_sexe
                * (self.poids**0.48)
                * ((self.taille / 100) ** 0.50)
                * (self.age ** (-0.13))
            )
        return self._mb

    def besoins_quotidiens(self):
        """
        Calcule la dépense énergétique quotidienne, hors activités sportives.
        """
        return self.metabolisme_base() * self.nap
