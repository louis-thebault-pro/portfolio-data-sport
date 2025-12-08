# -*- coding: utf-8 -*-
import pytest

from optimisation_nutrition.modeles.attributs import TypeActivite
from optimisation_nutrition.modeles.utils import conversion_enum, valeurs_enum


def test_valeurs_enum_contains_values():
    vals = valeurs_enum(TypeActivite)
    assert isinstance(vals, list)
    assert "endurance" in vals
    assert "force" in vals


def test_conversion_enum_accepts_various_casing():
    assert conversion_enum("Endurance", TypeActivite) == TypeActivite.ENDURANCE
    assert conversion_enum("ENDURANCE", TypeActivite) == TypeActivite.ENDURANCE
    assert conversion_enum(" endurance ", TypeActivite) == TypeActivite.ENDURANCE
    assert conversion_enum(TypeActivite.FORCE, TypeActivite) == TypeActivite.FORCE


def test_conversion_enum_none_and_invalid():
    assert conversion_enum(None, TypeActivite) is None
    with pytest.raises(ValueError):
        conversion_enum("inexistant-activite", TypeActivite)
