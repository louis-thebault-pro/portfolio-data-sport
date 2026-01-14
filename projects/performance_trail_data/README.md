# Analyse de la performance sportive en course à pied (trail et route)

## Objectif du projet
Ce projet vise à comprendre et prédire la performance en course à pied à partir de données d’activités sportives et physiologiques.
Le pipeline de données repose sur cinq grandes étapes : **Sources → Données brutes → Opérations → Informations → Actions**.
La finalité de ce projet sera la construction d'un outil capable d’expliquer la performance passée, d’évaluer la forme actuelle et de prédire les adaptations futures à l’entraînement.

---

## Méthodologie

Le développement de ce projet suit une approche incrémentale et exploratoire :
1. **Extraction et exploration initiale** des fichiers `.FIT` : structure, nettoyage, premières corrélations
2. **Analyse d’une activité unique** : mise en relation des données (FC, allure, dénivelé, etc.)
3. **Analyse multi-activités** : analyse de charge, comparaison des séances, identification de tendances
4. **Croisement avec les données quotidiennes** : sommeil, stress, nutrition...
5. **Modélisation prédictive** : forme, performance, risque de blessure
6. **Visualisation** : rapports, dashboards, graphiques de suivi

---

## Pipeline de données

Attention, dans ce projet les données brutes ne sont pas versionnées (dossier `data/` ignoré par `.gitignore`). Un échantillon anonymisé ou réduit est disponible dans `data_sample/` pour reproduire les analyses.

### 1. Sources de données
| Type                                | Description                                                 | Exemple                       |
| ----------------------------------- | ----------------------------------------------------------- | ----------------------------- |
| **Montre & applications**           | Données issues de plateformes comme Garmin, Coros ou Strava | Fichiers `.FIT`, `.TCX`, API  |
| **Journal de bord / Questionnaire** | Données subjectives renseignées manuellement                | Fichier Excel / Google Sheet  |
| **Tests de laboratoire**            | Mesures physiologiques ponctuelles                          | VO₂max, FCmax, SV1, SV2, etc. |



### 2. Données brutes collectées
| Catégorie                               | Variables principales                                                                                                                                                                                                                                      |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Activités sportives**                 | Temps, GPS, dénivelé, distance, type de séance (footing, fractionné, course…), allure, fréquence cardiaque (FC), cadence, puissance, rapport vertical, fréquence respiratoire, calories, temps de contact au sol, RPE, évaluation de la forme, commentaire |
| **Données physiologiques quotidiennes** | Sommeil, variabilité de la fréquence cardiaque (VFC), fréquence cardiaque au repos (FCR), niveau de stress, nombre de pas, calories au repos                                                                                                               |
| **Journal / bien-être**                 | Qualité de l’alimentation, humeur, symptômes (blessure, maladie), cycle menstruel                                                                                                                                                                          |
| **Tests de laboratoire**                | VO₂max, FCmax, SV1, SV2, etc.                                                                                                                                                                                                                              |

### 3. Opérations de traitement
Les opérations dépendront de la phase d’exploration, mais incluent notamment :
- **Nettoyage** des données (`NaN`, valeurs aberrantes, synchronisation des fréquences)
- **Fusion** des sources (liage par date ou identifiant d’activité)
- **Transformation** en métriques exploitables (zones d’intensité, ratios, scores de variabilité)
- **Agrégation** par séance, par semaine ou par bloc d’entraînement
- **Calcul d’indicateurs personnalisés** (charge, efficacité, dérive cardiaque, etc.)

### 4. Informations et analyses produites
| Objectif                      | Description                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Rapport de forme physique** | Identifier les tendances de progression, la cohérence des charges, les liens entre performance et données physiologiques |
| **Profil de l’athlète**       | Identifier les forces, faiblesses, sensibilités à la charge, et les moments les plus propices à l’entraînement           |
| **Prédiction de performance** | Modéliser les temps ou indices de performance futurs à partir du profil de l’athlète et de son historique                |

### 5. Finalités et actions
| Domaine                            | Applications concrètes                                                                 |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| **Optimisation de l’entraînement** | Ajustement des charges, suivi des phases de récupération, prévention de la blessure    |
| **Pacing & stratégie de course**   | Création de plans de course personnalisés en fonction du profil et des conditions      |
| **Planification saisonnière**      | Adaptation du calendrier de compétitions en fonction de la forme et de la récupération |

---

## Résultats (à venir)

Les premiers résultats attendus :
- Analyse de la relation entre allure, FC, dénivelé et puissance
- Visualisation de la progression et dérive cardiaque
- Estimation des zones de charge optimales
- Création d’un profil de coureur personnalisé

---

## Environnement & outils
- **IDE** : [VS Code](https://code.visualstudio.com/)
- **Langage** : [Python 3.13.8](https://www.python.org/downloads/release/python-3138/)
- **Librairies principales** :
  - `pandas` — manipulation et nettoyage des données
  - `numpy` — calculs scientifiques
  - `matplotlib` / `seaborn` — visualisation
  - `scikit-learn` — modélisation et analyse statistique
  - `fitparse` — lecture de fichiers `.FIT` (données Garmin/Coros)

---

## Structure du projet

```bash
performance_trail_data/
  ├── data_sample/         # Données anonymisées ou d’exemple
  ├── notebooks/           # Analyses exploratoires (Jupyter)
      ├── 01_exploration.ipynb
      └── 02_modelisation.ipynb
  ├── scripts/             # Scripts Python (traitement, calculs)
      ├── jumeau_numerique/
          ├── activités.py
          ├── athlete.py
          └── __init__.py
      └── main.py
  ├── resultats/           # Graphiques, rapports, exports
  ├── requirements.txt     # Dépendances Python
  └── README.md            # Présent fichier
```

---

## Licence
Ce portfolio est sous licence [MIT](LICENSE).

---

## Auteur

Projet développé par Louis Thébault dans le cadre d’un portfolio de projets informatiques appliqués au sport.

🔗 Voir l’ensemble du portfolio : [Portfolio de Louis Thébault](../../README.md)
