"""
Module définissant la classe Activite.

Attributs de la classe :
- description : str --> description explicite de l'activité
- type : TypeActivite --> type de l'activité (endurance, force, etc.)
- duree : float --> durée hebdomadaire de l'activité en heures
- met : float --> MET (Metabolic Equivalent Task) associé à l'activité

Méthodes :
- calcul_depense() --> calcule la dépense énergétique hebdomadaire sans prendre en compte le poids

"""

from pydantic import BaseModel, Field

from ._attributs import TypeActivité


class Activité(BaseModel):
    description: str = Field(..., title="Description de l'activité")
    type: TypeActivité = Field(
        TypeActivité.AUTRE,
        description="Type de l'activité à choisir entre endurance, force, etc. (Par défaut : 'autre')",
    )
    duree: float = Field(
        ..., gt=0, description="Durée de l'activité à renseigner en heures (>0)"
    )
    met: float = Field(
        ...,
        gt=0,
        description="Valeur MET de l'activité issue des tables de données (>0)",
    )
    """
    Propriétés de Field :
        - ... = valeur obligatoire, pas de valeur par défaut
        - gt = "greater than" : assure que la valeur est strictement supérieure à 0
        - Autres contraintes possibles : ge (greater or equal), le, lt, max_length, regex.
    """

    class Config:
        """Modification du comportement par défaut de Pydantic"""

        use_enum_values = True  # Utilisation de la valeur de l'énumération ("endurance" plutôt que TypeActivité.ENDURANCE)
        validate_assignment = (
            True  # Relance une validation lors de la modification d'un attribut
        )

    def calcul_depense(self) -> float:
        """
        Calcule la dépense énergétique liée à l'activité sans prendre en compte le poids.
        Formule : dépense = MET * durée
        """
        return self.met * self.duree

    def __str__(self):
        return f"{self.description} ({self.type}) - {self.duree:.1f}h - {self.met} METs"
