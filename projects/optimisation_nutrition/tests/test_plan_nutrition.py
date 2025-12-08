# -*- coding: utf-8 -*-
from optimisation_nutrition import (
    Activite,
    Nutrition,
    Personne,
)


def test_recommandations():
    p = Personne(poids=70, taille=175, age=30, sexe="Homme")
    a1 = Activite(description="Course", type="Endurance", duree=5, met=9.8)
    plan = Nutrition(personne=p, activites=[a1])

    a2 = Activite(description="Muscu", type="Force", duree=4, met=6)
    a3 = Activite(description="Course2", type="Endurance", duree=6, met=5)

    plan.ajouter_activite(a2)
    plan.ajouter_activite(a3)

    assert plan.besoins_quotidiens() > p.metabolisme_base()
