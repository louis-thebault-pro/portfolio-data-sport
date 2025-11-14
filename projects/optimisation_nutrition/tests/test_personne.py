from optimisation_nutrition import Personne


def test_MB_femme():
    pf = Personne(poids=60, taille=160, age=30, sexe="Femme")
    mb = pf.metabolisme_base()
    assert 1000 < mb < 1600


def test_mb_homme():
    ph = Personne(poids=70, taille=180, age=25, sexe="Homme")
    mb = ph.metabolisme_base()
    assert 1500 < mb < 2000
