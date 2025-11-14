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
    nutrition.ajouter_activite(
        Activite(description="Footing 1", type="Endurance", duree=45, met=8)
    )
    nutrition.ajouter_activite(
        Activite(description="Footing 2", type="Endurance", duree=45, met=8)
    )
    nutrition.ajouter_activite(
        Activite(description="Sortie longue", type="Endurance", duree=90, met=8)
    )
    nutrition.ajouter_activite(
        Activite(description="Fractionné", type="Endurance", duree=50, met=13)
    )
    nutrition.ajouter_activite(
        Activite(description="Musculation 1", type="Force", duree=60, met=3)
    )
    nutrition.ajouter_activite(
        Activite(description="Musculation 2", type="Force", duree=60, met=3)
    )
    nutrition.ajouter_activite(
        Activite(description="Football", type="Intermittent", duree=90, met=9)
    )

    i = 1
    for activite in nutrition.activites:
        print(f"Activité {i} : {activite}")
        i += 1

    print(nutrition.recommandations_personne())
    print(nutrition.plan_nutrition())


if __name__ == "__main__":
    main()
