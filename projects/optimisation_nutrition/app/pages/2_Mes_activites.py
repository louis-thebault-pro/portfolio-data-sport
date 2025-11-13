import streamlit as st

from optimisation_nutrition import Activite
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
    v: ["Type de type 1", "Type de type 2"] for v in valeurs_enum(TypeActivite)
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
    st.success("Activité ajoutée avec succès")


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
                st.text_input(
                    "Nom de l'activité", placeholder="Ex: Footing", key="description"
                )
            with col2:
                type = st.selectbox(
                    "Type d'activité",
                    options=list(TYPES_ACTIVITES.keys()),
                    key="type",
                )
            with col3:
                st.selectbox(
                    "Détail de l'activité",
                    options=TYPES_ACTIVITES.get(type, []),
                    index=0,
                    key="detail_activite",
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
