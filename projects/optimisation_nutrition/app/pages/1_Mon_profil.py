import streamlit as st
from pydantic import ValidationError

from optimisation_nutrition import Personne

st.title("Mon profil")

with st.form("formulaire_profil"):
    st.subheader("Informations personnelles")

    prenom = st.text_input("Prénom")
    nom = st.text_input("Nom")
    sexe = st.selectbox("Sexe", options=["Femme", "Homme", "Non renseigné"], index=None)
    age = st.number_input("Âge", 1, 120, 30)
    taille = st.number_input("Taille (cm)", 1, 280, 165)
    poids = st.number_input("Poids (kg)", 1, 650, 65)
    regime = st.selectbox(
        "Régime alimentaire",
        options=["Omnivore", "Pesco-végétarien", "Végétarien", "Végétalien"],
    )
    objectif = st.selectbox(
        "Objectif personnel",
        options=["Maintien du poids", "Prise de masse", "Perte de poids"],
    )

    submit = st.form_submit_button("Valider mon profil")

if submit:
    try:
        personne = Personne(
            prenom=prenom,
            nom=nom,
            age=age,
            sexe=sexe,
            poids=poids,
            taille=taille,
            regime=regime,
            objectif=objectif,
        )
        st.success("Ton profil a bien été enregistré")
        st.write(personne)
        st.session_state["personne"] = personne

    except ValidationError as e:
        st.error("Certains champs sont mal remplis, peux-tu vérifier ?")
        for err in e.errors():
            st.warning(f"{err['loc'][0]} : {err['msg']}")
