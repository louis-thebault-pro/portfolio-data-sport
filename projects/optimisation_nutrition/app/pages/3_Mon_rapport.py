import streamlit as st

from optimisation_nutrition import Nutrition

if "nutrition" not in st.session_state:
    st.session_state.nutrition = None
if "personne" in st.session_state:
    st.session_state.nutrition = Nutrition(
        personne=st.session_state.personne,
        activites=(
            st.session_state.activites if "activites" in st.session_state else []
        ),
    )


st.title("Rapport nutritionnel")


nutrition = st.session_state.nutrition
st.markdown(
    f"""
    Métabolisme de base (par jour) : {nutrition.metabolisme_base()} kcal
    \n\nBesoins énergétiques hebdomadaires : {nutrition.besoins_hebdomadaires()} kcal
    \n\nBesoins énergétiques quotidiens : {nutrition.besoins_quotidiens()} kcal
    """
)
