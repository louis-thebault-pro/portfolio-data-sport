# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st

from optimisation_nutrition import Nutrition

st.title("Rapport nutritionnel")

if "nutrition" not in st.session_state:
    st.session_state.nutrition = None
if "personne" not in st.session_state:
    st.session_state.personne = None

if st.session_state.personne:

    nutrition = Nutrition(
        personne=st.session_state.personne,
        activites=(
            st.session_state.activites if "activites" in st.session_state else []
        ),
    )
    st.session_state.nutrition = nutrition

    st.write(
        f"""
        Cette semaine, tu as besoin de manger l'équivalent de {int(nutrition.besoins_hebdomadaires())} kcal.
        Par jour, cela représente {nutrition.besoins_quotidiens()} kcal.
        """
    )

    besoins = nutrition.plan_nutrition()
    col1, col2 = st.columns(2)
    with col1:
        st.write("Chaque jour, tes besoins en macro-nutriments sont :")
        for cle in besoins:
            st.write(f" - {cle} : {besoins[cle]["absolu"]} g")

    with col2:

        donnees, labels = [], []
        for cle in besoins:
            if "pourcentage_reel" in besoins[cle]:
                donnees.append(besoins[cle]["pourcentage_reel"])
                labels.append(cle)

        fig, ax = plt.subplots()
        ax.pie(donnees, labels=labels, autopct="%1.1f%%")
        ax.axis("equal")

        st.write("Voici la composition de ton assiette type :")
        st.pyplot(fig)

    if nutrition.activites == []:
        st.warning("Attention, tu n'as rempli aucune activité sportive")


else:
    st.error(
        "Tu vas un peu vite en besogne !\nAvant d'obtenir ton rapport, remplis et valide ton profil."
    )
