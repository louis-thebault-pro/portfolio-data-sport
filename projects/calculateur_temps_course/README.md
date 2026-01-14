# Calculateur de temps en course à pied sur route (Excel)

## Objectif
Ce projet vise à créer un outil de prédiction de performance en course à pied, basé sur un temps de référence et intégrant l’impact d’un entraînement futur (durée, volume et typologie des séances). L’objectif n’est pas de fournir une prédiction exacte, mais une estimation cohérente et réaliste.
L’outil est implémenté sous Excel, outil accessible, transparent et facilement modifiable.

---

## Méthodologie
Le modèle repose sur plusieurs briques complémentaires :
1. Le niveau actuel (utilisation de la formule de Riegel pour estimer les performances sur différentes distances à partir d’un temps de référence et calcul de l’allure associée (min/km)
2. La modélisation de l’entraînement futur en tenant compte :
   1. du nombre de semaines jusqu’à l’objectif
   2. du nombre de séances par semaine
   3. de la typologie des séances (footing, sortie longue, fractionné)
   4. du caractère spécifique ou non de la préparation.
3. Une séparation des effets d’entraînement (distinction entre une adaptation générale et une adaptation spécifique à la distance objectif)
4. Des garde-fous de réalisme (pondération selon le niveau initial de l’athlète, pénalisation des préparations non spécifiques, paramètres calibrés pour éviter des gains irréalistes, en particulier sur les longues distances.

---

## Structure de l'outil
Le classeur Excel est structuré en 3 feuilles :
1. *Entrées utilisateur* qui permet d'entrer le temps, la distance de référence, l'objectif (distance) et les paramètres d’entraînement (durée, volume, type de séances, spécificité)
2. *Estimation du temps* qui permet de visualiser une estimation de son temps et les allures prévus pour différentes distances au moment de l'objectif, une comparaison du niveau actuel avec le niveau projeté, tout en pouvant voyant les calculs intermédiaires permettant d'arriver à ce calcul
3. *Paramètres* qui regroupe l'ensemble des paramètres du modèle

---

## Résultats
L’outil permet d’obtenir des ordres de grandeur plausibles de progression, de visualiser l’impact d’une préparation plus longue, d’une augmentation du volume ou d’un entraînement plus spécifique.

Les résultats sont basées sur un modèle réfléchi mais empirique et doivent donc être interprétés comme des estimations indicatives, et non comme des prédictions garanties.

---

## Environnement & outils
- **Microsoft Excel**

---

## Licence
Ce portfolio est sous licence [MIT](LICENSE).

---

## Auteur

Projet développé par Louis Thébault, dans le cadre d’un portfolio de projets informatiques appliqués au sport.

Voir l’ensemble du portfolio : [Portfolio de Louis Thébault](../../README.md)