# -*- coding: utf-8 -*-
"""

Point d'entrée du code analysant les données

"""

from jumeau_numerique import Athlete
from datetime import date


def main():
    """Fonction principale exécutant le code."""

    athlete1 = Athlete(
        nom="Dupont",
        prenom="Léa",
        naissance=date(1992, 11, 3),
        poids=50,
        taille=160,
        sexe="NB",
        VMA=12,
        VO2max=45,
        FCrepos=55,
        FCmax=190,
        SV1=155,
        SV2=180,
        durabilité=0,
        activités={},
    )
    print(athlete1)


if __name__ == "__main__":
    main()
