# -*- coding: utf-8 -*-
"""
Paquet regroupant les données et fonctions permettant d'accéder à celles-ci.

Structure du paquet :
modeles/
├── __init__.py
├── recommandations.json (Données des recommandations en macro et micro-nutriments en fonction du sport)
└── recommandations.py (Fonctions d'accès aux données du fichier json 'recommandations')
"""

from .donnees import (
    MET,
    get_cas_particulier,
    get_fourchette,
    get_profil,
    lire_json,
)

__all__ = [
    "lire_json",
    "get_profil",
    "get_cas_particulier",
    "get_fourchette",
    "MET",
]
