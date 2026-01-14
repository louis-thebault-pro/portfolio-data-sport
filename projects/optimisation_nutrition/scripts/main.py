# -*- coding: utf-8 -*-
"""
Point d'entrée du programme

"""

from optimisation_nutrition import Activite, Nutrition, Personne


def main():
    """Fonction principale exécutant le programme."""

    personne = Personne(
        prenom="prenom",
        nom="nom",
        sexe="Homme",
        age=26,
        poids=74,
        taille=178,
        regime="Pesco-végétarien",
        nap=1.6,
    )

    nutrition = Nutrition(personne=personne)
    nutrition.ajouter_activite(Activite(duree=45))
    nutrition.ajouter_activite(Activite(duree=90))
    nutrition.ajouter_activite(Activite(duree=50))
    nutrition.ajouter_activite(Activite(duree=60))

    for i, activite in enumerate(nutrition.activites):
        print(f"{i+1} : {activite}")

    print(nutrition.recommandations_personne())
    print(nutrition.plan_nutrition())


if __name__ == "__main__":
    main()
