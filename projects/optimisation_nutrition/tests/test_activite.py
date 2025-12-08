# -*- coding: utf-8 -*-
from optimisation_nutrition import Activite


def test_MB_femme():
    a = Activite(description="Course", type="Endurance", duree=30, met=4)
    assert a.calcul_depense() == 2.0
