import streamlit as st

st.set_page_config(page_title="Calcul besoins énergétiques", layout="wide")
st.title("Application pour le calcul de ses besoins nutritionnels")
st.markdown(
    """
Bienvenue dans ton assistant d'optimisation nutritionnelle. Celui-ci va t'aider à calculer tes besoins nutritionnels en fonction de ton profil et des tes activités.
\n\n Utilise le menu à gauche pour :
            \n1. Créer ton profil utilisateur
            \n2. Ajouter tes activités
            \n3. Visualiser et génrer ton rapport nutritionnel
            """
)
