# Calculateur des besoins nutritionnels en fonction des données anthropométriques et de l'activité hebdomadaire

## Objectif du projet
Ce projet a pour objectif de modéliser des recommandations nutritionnelles personnalisées en fonction :
- du profil individuel (âge, sexe, taille, poids, objectif)
- du niveau d’activité quotidienne hors sport (NAP)
- des activités sportives pratiquées (type, durée, intensité)

L’idée est de créer un outil de modélisation, basé sur la science, permettant de calculer simplement les besoins et de les transformer en recommandations fiables et exploitables par l'utilisateur.

L'objectif final de ce projet, au-delà de la simple modélisation, serait de construire un **outil permettant d'anticiper les besoins nutritionnel en fonction des périodes d'entraînement à venir, et de proposer les menus les plus adaptés**.

---

## Méthodologie
Ce projet a été construit suivant une architecture assez classique :
- le **backend** regroupant toute la logique métier, de la manipulation des données aux différents calculs
- le **frontend** sous la forme d'une interface Streamlit permettant d'utiliser l'outil le plus simplement possible

Pour la logique métier du backend, plusieurs objets sont utilisés :
1. Le **profil utilisateur** qui regroupe les données anthropométriques, l'objectif nutritionnel, le régime alimentaire et le niveau d’activité quotidienne hors sport (NAP)
2. Les **activités physiques** définies chacunes par un type (endurance, force, intermittent, combat, etc.), une durée, une intensité et la dépense énergétique estimée (via une base de données des METs). Ces activités sont ensuite agrégées pour déterminer le poids relatif de chaque type d'activité, calculer l'intensité moyenner par type et pondérer les recommandations nutritionnelles.
3. Le **calcul des besoins énergétiques**, selon la logique suivante : *DEJ = Métabolisme de base × NAP  +  Dépenses liées aux activités sportives*.
4. Les **recommandations nutritionnelles** calculés suivant les éléments précédents et basés sur des données issues de la littérature scientifique et regroupées dans des bases de données .xlsx et .JSON.
La logique appliquée pour réaliser les différentes recommandations est la suivante :
- les glucides sont prioritairement influencés par l’endurance
- les protéines par la force et les sports intermittents
- les lipides restent plus stables et servent de variable d’équilibrage
Lorsque plusieurs types d’activités coexistent, les recommandations sont pondérées selon le poids énergétique de chaque type.

L'interface utilisateur, codée dans le frontend, est une interface *Streamlit* assez simple permettant de saisir le profil utilisateur, d'ajouter ou modifier des activités sportives et d'afficher les recommandations.

---

## Structure du projet
```bash
optimisation_nutrition/
  ├── app/                    # frontend
      ├── pages/              # 3 pages Streamlit
          ├── 1_Mon_profil.py
          ├── 2_Mes_activites.py
          └── 3_Mon_rapport.py
      ├── app.py
      └── __init__.py
  ├── optimisation_nutrition/ # backend
      ├── donnees/
          ├── MET.xlsx
          ├── NAP.JSON
          ├── recommandations.JSON
          ├── donnees.py
          └── __init__.py
      ├── modeles/
          ├── activite.py
          ├── attributs.py
          ├── nutrition.py
          ├── personne.py
          ├── utils.py
          └── __init__.py
      └── __init__.py
  ├── scripts/              # lancement des calculs hors interface
      ├── main.py
      └── __init__.py
  ├── requirements.txt
  └── README.md
```

---

## Résultats et perspectives
Le système produit pour l'instant :
- des recommandations (uniquement macronutriments) en valeurs absolues (g/j)
- des pourcentages énergétiques calculés à partir des valeurs absolues
- une comparaison avec les plages recommandées afin d’évaluer la cohérence

Il existe plusieurs perspectives d'évolution du produit :
- intégration d'un calcul des besoins en micronutriments
- export PDF des recommandations
- anticipation des besoins nutritionnels en fonction du programme de l'athlète
- conception de menus hebdomadaires permettant de couvrir les besoins en fonction du régime alimentaire de l'athlète

---

## Environnement & outils
- **IDE** : [VS Code](https://code.visualstudio.com/)
- **Langage** : [Python 3.13.8](https://www.python.org/downloads/release/python-3138/)
- **Librairies principales utilisées** :
  - Pydantic
  - Streamlit

---

## Licence
Ce portfolio est sous licence [MIT](LICENSE).

---

## Auteur

Projet développé par Louis Thébault, dans le cadre d’un portfolio de projets informatiques appliqués au sport.

Voir l’ensemble du portfolio : [Portfolio de Louis Thébault](../../README.md)
