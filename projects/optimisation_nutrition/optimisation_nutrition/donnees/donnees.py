# -*- coding: utf-8 -*-
import json

import pandas as pd


def lire_excel(chemin: str):
    donnees = pd.read_excel(chemin)
    return donnees


def lire_json(chemin: str):
    with open(chemin, encoding="utf-8") as f:
        datas = json.load(f)
        return datas


def get_profil(profil: str, datas: dict):
    return datas[profil] if profil in datas else None


def get_cas_particulier(
    profil: dict,
    cas_general: dict = {
        "glucide": ["absolu", "pourcentage"],
        "proteine": ["absolu", "pourcentage"],
        "lipide": ["absolu", "pourcentage", "composition"],
        "fibres": ["absolu", "composition"],
    },
    type_nutriment: str = "macro",
):
    """Fonction permettant de savoir si des cas particuliers liés au type de sport se trouve dans les recommandations."""
    particulier = {}
    nutriments = profil[type_nutriment]
    for nutriment in nutriments:
        cas_part_nutriment = []
        for element in nutriments[nutriment]:
            if element not in cas_general[nutriment]:
                cas_part_nutriment.append(
                    element
                )  # Si l'élément diffère du cas général, on l'ajoute à la liste
        if cas_part_nutriment != []:  # Si des éléments particuliers existent
            particulier[nutriment] = (
                cas_part_nutriment  # On ajoute la liste au dict avec le type de macro en clé
            )
    return (
        None if particulier == {} else particulier
    )  # Renvoie None si pas de cas particulier, le dict des cas particuliers sinon


def get_fourchette(profil: dict, nutriment: str, type: str = "absolu"):
    for type_nutriment in profil:
        nutriments = profil[type_nutriment]
        if nutriment in nutriments:
            valeurs = nutriments[nutriment][type]
            return (valeurs["min"], valeurs["max"])
    return None
