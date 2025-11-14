"""
Point d'entrée du programme

"""

from optimisation_nutrition import Activite, Nutrition, Personne


def main():
    """Fonction principale exécutant le programme."""

    louis = Personne(
        prenom="Louis",
        nom="Thébault",
        sexe="Homme",
        age=26,
        poids=74,
        taille=178,
        regime="Pesco-végétarien",
    )

    nutrition = Nutrition(personne=louis)
    nutrition.ajouter_activite(
        Activite(description="Footing", type="Endurance", duree=60, met=5)
    )
    nutrition.ajouter_activite(
        Activite(description="Footing", type="Endurance", duree=120, met=5)
    )
    # nutrition.ajouter_activite(
    #     Activite(description="Footing", type="Endurance", duree=20, met=5)
    # )
    nutrition.ajouter_activite(
        Activite(description="Musculation", type="Force", duree=58, met=6)
    )
    nutrition.ajouter_activite(
        Activite(description="Football", type="Intermittent", duree=120, met=4)
    )

    i = 1
    for activite in nutrition.activites:
        print(f"Activité {i} : {activite}")
        i += 1

    print(nutrition.recommandations_personne())


if __name__ == "__main__":
    main()
