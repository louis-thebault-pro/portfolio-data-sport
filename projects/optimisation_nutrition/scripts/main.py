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
        poids=70,
        taille=178,
        regime="Pesco-végétarien",
    )
    print(louis)

    nutrition = Nutrition(personne=louis)
    nutrition.ajouter_activite(
        Activite(description="Footing", type="Endurance", duree=45, met=10)
    )
    nutrition.ajouter_activite(
        Activite(description="Footing", type="Endurance", duree=30, met=5)
    )
    nutrition.ajouter_activite(
        Activite(description="Musculation", type="Force", duree=58, met=6)
    )

    i = 1
    for activite in nutrition.activites:
        print(f"Activité {i} : {activite}")
        i += 1

    print(nutrition)
    print(nutrition.recommandations_personne())


if __name__ == "__main__":
    main()
