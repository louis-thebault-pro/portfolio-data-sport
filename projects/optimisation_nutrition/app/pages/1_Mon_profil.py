import streamlit as st
from pydantic import ValidationError

from optimisation_nutrition import (
    ObjectifAlimentaire,
    Personne,
    RegimeAlimentaire,
    Sexe,
)

# Initialisation de la session Streamlit

if "personne" not in st.session_state:
    st.session_state["personne"] = None
if "edit_profile_mode" not in st.session_state:
    st.session_state["edit_profile_mode"] = True


# Définition des fonctions nécessaires pour le fonctionnement de la page Streamlit


def enregistrer_personne():
    """Fonction permettant d'enregistrer les données personnelles dans la variable du session_state 'personne' et de passer du mode 'édition' au mode 'profil'"""
    try:
        # Création de la personne avec ses données personnelles
        personne = Personne(
            prenom=st.session_state.get("prenom_input"),
            nom=st.session_state.get("nom_input"),
            age=st.session_state.get("age_input"),
            sexe=st.session_state.get("sexe_input"),
            poids=st.session_state.get("poids_input"),
            taille=st.session_state.get("taille_input"),
            regime=st.session_state.get("regime_input"),
            objectif=st.session_state.get("objectif_input"),
        )
        # Si la personne est bien créée, affichage du succès et enregistrement du profil
        st.success("Ton profil a bien été enregistré")
        st.session_state["personne"] = personne

        # Passage de la page en mode 'Profil' en modifiant la valeur de "edit_profile_mode"
        st.session_state["edit_profile_mode"] = False

    except ValidationError as e:
        # Si la création de la personne est impossible, affichage des erreurs
        st.error("Certains champs sont mal remplis, peux-tu vérifier ?")
        for err in e.errors():
            st.warning(f"{err['loc'][0]} : {err['msg']}")


def modifier_personne():
    """Fonction permettant de passer du mode 'profil' au mode 'édition' et inversement en modifiant la valeur de la variable du session_state 'edit_profile_mode'"""
    st.session_state["edit_profile_mode"] = True


def formulaire_profil(personne):
    """Fonction affichant le formulaire permettant à l'utilisateur de rentrer et valider ses données personnelles"""

    # Récupération des données possibles pour Sexe, Régime et Objectif
    options_sexe = [s.value for s in Sexe]
    options_regime = [r.value for r in RegimeAlimentaire]
    options_objectif = [o.value for o in ObjectifAlimentaire]

    # Création et/ou récupération des valeurs par défaut dans chaque champs du formulaire
    dico = {
        "prenom": "",
        "nom": "",
        "sexe": None,
        "age": 30,
        "taille": 165,
        "poids": 65.0,
        "regime": None,
        "objectif": None,
    }
    if not not personne:
        dico = {
            "prenom": personne.prenom,
            "nom": personne.nom,
            "sexe": options_sexe.index(personne.sexe),
            "age": personne.age,
            "taille": personne.taille,
            "poids": personne.poids,
            "regime": options_regime.index(personne.regime),
            "objectif": options_objectif.index(personne.objectif),
        }

    # Création du formulaire et enregistrement des valeurs avec différentes clés du session_state
    with st.form("formulaire_profil"):

        st.subheader("Informations personnelles")
        st.text_input("Prénom", value=dico["prenom"], key="prenom_input")
        st.text_input("Nom", value=dico["nom"], key="nom_input")
        st.selectbox("Sexe", options=options_sexe, index=dico["sexe"], key="sexe_input")
        st.number_input(
            "Âge",
            min_value=1,
            max_value=120,
            value=dico["age"],
            key="age_input",
        )
        st.number_input(
            "Taille (cm)",
            min_value=1,
            max_value=280,
            value=dico["taille"],
            key="taille_input",
        )
        st.number_input(
            "Poids (kg)",
            min_value=1.0,
            max_value=650.0,
            value=dico["poids"],
            step=0.1,
            key="poids_input",
        )
        st.selectbox(
            "Régime alimentaire",
            options=options_regime,
            index=dico["regime"],
            key="regime_input",
        )
        st.selectbox(
            "Objectif personnel",
            options=options_objectif,
            index=dico["objectif"],
            key="objectif_input",
        )

        # Bouton validant le formulaire en appelant la fonction enregistrer_personne()
        st.form_submit_button("Valider mon profil", on_click=enregistrer_personne)


# Initialisation et écriture de la page Streamlit

st.title("Mon profil")
personne = st.session_state["personne"]

# Cas 1 : mode édition
if st.session_state["edit_profile_mode"] or personne is None:
    # On affiche le formulaire de saisie des informations personnelles
    formulaire_profil(personne)

# Cas 2 : mode profil
else:
    # On affiche le profil
    st.write(f"**Prénom:** {personne.prenom}")
    st.write(f"**Nom:** {personne.nom}")
    st.write(f"**Sexe:** {personne.sexe}")
    st.write(f"**Âge:** {personne.age} ans")
    st.write(f"**Taille:** {personne.taille/100:.2f} m")
    st.write(f"**Poids:** {personne.poids:.1f} kg")
    st.write(f"**Régime alimentaire:** {personne.regime}")
    st.write(f"**Objectif:** {personne.objectif}")

    st.button("Modifier le profil", on_click=modifier_personne)
