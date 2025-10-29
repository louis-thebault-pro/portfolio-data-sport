from optimisation_nutrition import (
    Activite,
    Nutrition,
    Personne,
)


def test_calcul_depenses():
    p = Personne(poids=70, taille=175, age=30, sexe="homme")
    a1 = Activite(description="Course", duree=5, met=9.8)
    plan = Nutrition(personne=p, activites=[a1])

    assert plan.besoins_quotidiens() > p.metabolisme_base()
