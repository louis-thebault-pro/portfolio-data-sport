# -*- coding: utf-8 -*-
import streamlit as st

from optimisation_nutrition import Activite
from optimisation_nutrition.donnees import MET
from optimisation_nutrition.modeles.attributs import TypeActivite
from optimisation_nutrition.modeles.utils import valeurs_enum

# Initialisation de la page

if "activites" not in st.session_state:
    st.session_state.activites = []
if "ajout_activite" not in st.session_state:
    st.session_state.ajout_activite = False
if "niveau_vie_active" not in st.session_state:
    st.session_state.niveau_vie_active = 1
if "erreur_activite" not in st.session_state:
    st.session_state.erreur_activite = None


TYPES_ACTIVITES = {
    valeurs_enum(TypeActivite)[i]: ["Type de type 1", "Type de type 2"]
    for i in range(1, len(valeurs_enum(TypeActivite)))
}


# Définition des fonctions nécessaires pour le fonctionnement de la page


def _passer_en_ajout_activite():
    st.session_state.ajout_activite = True
    st.session_state.erreur_activite = None


def _supprimer_activite(index):
    st.session_state.activites.pop(index)


def _valider_activite():
    description = st.session_state.get("description", "").strip()
    duree = st.session_state.get("duree", 0)
    type_activite = st.session_state.get("type")
    if description == "" or type_activite == "":
        st.session_state.erreur_activite = (
            "Veuillez remplir tous les champs correctement."
        )
        return
    activite = Activite(description=description, type=type_activite, duree=duree, met=1)
    st.session_state.activites.append(activite)
    st.session_state.ajout_activite = False
    st.session_state.erreur_activite = None


def _annuler_ajout():
    st.session_state.ajout_activite = False
    st.session_state.erreur_activite = None


def afficher_activites():
    if st.session_state.activites:
        for i, activite in enumerate(st.session_state.activites):
            with st.container():
                type_str = (
                    activite.type.value
                    if hasattr(activite.type, "value")
                    else str(activite.type)
                )
                st.write(
                    f"Activité {i+1} : {activite.description} ({type_str}), {activite.duree} minutes"
                )
                st.button(
                    "Supprimer",
                    key=f"supprimer_{i}",
                    on_click=_supprimer_activite,
                    args=(i,),
                )
        st.divider()


def form_ajout_activite():
    if not st.session_state.ajout_activite:
        st.button("Ajouter une activité", on_click=_passer_en_ajout_activite)
    else:
        st.markdown("#### Nouvelle activité")

        with st.form("activite"):
            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)
            col5, col6 = st.columns(2)
            with col1:
                sport_options = list(MET.keys())
                default_sport = st.session_state.get(
                    "sport", sport_options[0] if sport_options else None
                )
                sport_index = (
                    sport_options.index(default_sport)
                    if default_sport in sport_options
                    else 0
                )
                sport = st.selectbox(
                    "Sport",
                    options=sport_options,
                    index=sport_index,
                    key="sport",
                )
                st.write(sport)
            with col2:
                st.write(sport)
            with col3:
                current_sport = sport or (sport_options[0] if sport_options else None)
                description_options = (
                    list(MET.get(current_sport, {}).keys()) if current_sport else []
                )
                st.selectbox(
                    "Description de l'activité",
                    options=description_options,
                    index=0 if description_options else None,
                    key="description_activite",
                )
            with col4:
                st.number_input(
                    "Durée (minutes)",
                    min_value=1,
                    step=1,
                    value=30,
                    key="duree",
                )
            with col5:
                st.form_submit_button("Valider l'activité", on_click=_valider_activite)
            with col6:
                st.form_submit_button("Annuler", on_click=_annuler_ajout)
            if st.session_state.get("erreur_activite"):
                st.error(st.session_state.get("erreur_activite"))


# Ecriture de la page

st.title("Mes activités hebdomadaires")

st.markdown("### Activités :")
afficher_activites()
form_ajout_activite()
