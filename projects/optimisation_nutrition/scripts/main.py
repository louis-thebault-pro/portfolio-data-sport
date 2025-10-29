"""
Point d'entrée du programme

"""

from optimisation_nutrition import Activite, Nutrition, Personne


def main():
    """Fonction principale exécutant le programme."""

    louis = Personne(
        prenom="Louis",
        nom="Thébault",
        sexe="homme",
        poids=70,
        taille=178,
        regime="pesco-végétarien",
    )
    print(louis)

    nutrition = Nutrition(personne=louis)
    nutrition.ajouter_activite(
        Activite(description="Footing", type="endurance", duree=45, met=9.8)
    )
    nutrition.ajouter_activite(
        Activite(description="Musculation", type="force", duree=58, met=6)
    )

    for activite in nutrition.activites:
        print(activite)

    print(nutrition)


if __name__ == "__main__":
    main()
