# -*- coding: utf-8 -*-
import streamlit as st
from pydantic import ValidationError

from optimisation_nutrition import Personne
from optimisation_nutrition.donnees import lire_json
from optimisation_nutrition.modeles.attributs import (
    ObjectifAlimentaire,
    RegimeAlimentaire,
    Sexe,
)
from optimisation_nutrition.modeles.utils import valeurs_enum

# Initialisation de la page

if "personne" not in st.session_state:
    st.session_state.personne = None
if "mode_edition_profil" not in st.session_state:
    st.session_state.mode_edition_profil = True
if "erreur_profil" not in st.session_state:
    st.session_state.erreur_profil = None
if "niveau_activite" not in st.session_state:
    st.session_state.niveau_activite = 1
if "mode_edition_niveau_activite" not in st.session_state:
    st.session_state.mode_edition_niveau_activite = True

NAP = lire_json("optimisation_nutrition/donnees/NAP.JSON")
NIVEAU_ACTIVITE = {}
for cle in NAP:
    NIVEAU_ACTIVITE[NAP[cle]["nap"]] = NAP[cle]["description"]


# Définition des fonctions nécessaires pour le fonctionnement de la page


def _enregistrer_personne():
    """Fonction permettant d'enregistrer les données personnelles dans la variable du session_state 'personne' et de passer du mode 'édition' au mode 'profil'"""
    try:
        # Création de la personne avec ses données personnelles
        personne = Personne(
            prenom=st.session_state.get("prenom"),
            nom=st.session_state.get("nom"),
            age=st.session_state.get("age"),
            sexe=st.session_state.get("sexe"),
            poids=st.session_state.get("poids"),
            taille=st.session_state.get("taille"),
            regime=st.session_state.get("regime"),
            objectif=st.session_state.get("objectif"),
            nap=st.session_state.get("nap"),
        )
        # Si la personne est bien créée, enregistrement du profil
        st.session_state.personne = personne

        # Passage de la page en mode 'Profil'
        _passer_mode_profil()

    except ValidationError:
        # Si la création de la personne est impossible, affichage des erreurs
        st.session_state.erreur_profil = (
            "Hop hop hop, tu n'as pas rempli tous les champs correctement..."
        )
        return


def _modifier_personne():
    """Fonction permettant de passer du mode 'profil' au mode 'édition' et inversement en modifiant la valeur de la variable du session_state 'edit_profile_mode'"""
    st.session_state.mode_edition_profil = True
    st.session_state.erreur_profil = None


def _passer_mode_profil():
    st.session_state.mode_edition_profil = False
    st.session_state.erreur_profil = None


def _champs_par_defaut(personne, options_sexe, options_regime, options_objectif):
    """Fonction permettant de créer ou récupérer des valeurs par défaut pour les champs du formulaire"""
    cles_nap = list(NIVEAU_ACTIVITE.keys())
    return (
        {
            "prenom": personne.prenom,
            "nom": personne.nom,
            "sexe": options_sexe.index(
                personne.sexe.value
                if hasattr(personne.sexe, "value")
                else personne.sexe
            ),
            "age": personne.age,
            "taille": personne.taille,
            "poids": personne.poids,
            "regime": options_regime.index(
                personne.regime.value
                if hasattr(personne.regime, "value")
                else personne.regime
            ),
            "objectif": options_objectif.index(
                personne.objectif.value
                if hasattr(personne.objectif, "value")
                else personne.objectif
            ),
            "nap": cles_nap.index(personne.nap),
        }
        if personne
        else {
            "prenom": "",
            "nom": "",
            "sexe": None,
            "age": 30,
            "taille": 165,
            "poids": 65.0,
            "regime": None,
            "objectif": None,
            "nap": 0,
        }
    )


def form_profil(personne):
    """Fonction affichant le formulaire permettant à l'utilisateur de rentrer et valider ses données personnelles"""

    # Récupération des données possibles pour Sexe, Régime et Objectif
    options_sexe = valeurs_enum(Sexe)
    options_regime = valeurs_enum(RegimeAlimentaire)
    options_objectif = valeurs_enum(ObjectifAlimentaire)

    # Récupération des champs par défaut
    defaut = _champs_par_defaut(
        personne, options_sexe, options_regime, options_objectif
    )

    # Création du formulaire et enregistrement des valeurs avec différentes clés du session_state
    with st.form("formulaire_profil"):

        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Prénom", value=defaut["prenom"], key="prenom")
        with col2:
            st.text_input("Nom", value=defaut["nom"], key="nom")

        col3, col4 = st.columns(2)
        with col3:
            st.selectbox("Sexe", options=options_sexe, index=defaut["sexe"], key="sexe")
        with col4:
            st.number_input(
                "Âge",
                min_value=1,
                max_value=120,
                value=defaut["age"],
                key="age",
            )

        col5, col6 = st.columns(2)
        with col5:
            st.number_input(
                "Taille (cm)",
                min_value=1,
                max_value=280,
                value=defaut["taille"],
                key="taille",
            )
        with col6:
            st.number_input(
                "Poids (kg)",
                min_value=1.0,
                max_value=650.0,
                value=defaut["poids"],
                step=0.1,
                key="poids",
            )

        col7, col8 = st.columns(2)
        with col7:
            st.selectbox(
                "Régime alimentaire",
                options=options_regime,
                index=defaut["regime"],
                key="regime",
            )
        with col8:
            st.selectbox(
                "Objectif personnel",
                options=options_objectif,
                index=defaut["objectif"],
                key="objectif",
            )

        st.radio(
            label="Niveau d'activité au quotidien (hors activités sportives) :",
            index=defaut["nap"],
            options=NIVEAU_ACTIVITE.keys(),
            format_func=lambda x: NIVEAU_ACTIVITE[x],
            horizontal=False,
            key="nap",
        )

        col1, col2, col3 = st.columns(3)
        with col2:
            st.form_submit_button("Valider les infos", on_click=_enregistrer_personne)
        if st.session_state.get("erreur_profil"):
            st.error(st.session_state.get("erreur_profil"))


def afficher_profil(personne):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Prénom:** {personne.prenom}")
            st.write(
                f"**Sexe:** {personne.sexe.value if hasattr(personne.sexe, 'value') else personne.sexe}"
            )
            st.write(f"**Taille:** {personne.taille/100:.2f} m")
            st.write(
                f"**Régime alimentaire:** {personne.regime.value if hasattr(personne.regime, 'value') else personne.regime}"
            )

        with col2:
            st.write(f"**Nom:** {personne.nom}")
            st.write(f"**Âge:** {personne.age} ans")
            st.write(f"**Poids:** {personne.poids:.1f} kg")
            st.write(
                f"**Objectif:** {personne.objectif.value if hasattr(personne.objectif, 'value') else personne.objectif}"
            )
        st.write(f"**Niveau d'activité:** {NIVEAU_ACTIVITE.get(personne.nap)}")

        st.button("Modifier mes infos", on_click=_modifier_personne)


# Ecriture de la page

st.title("Mon profil")

personne = st.session_state.personne
if st.session_state.mode_edition_profil or not personne:
    # On affiche le formulaire de saisie des informations personnelles
    form_profil(personne)
else:
    # On affiche le profil
    afficher_profil(personne)
