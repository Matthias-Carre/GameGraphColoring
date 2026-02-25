# Jeu de coloration sur les grilles

## Description

Ce projet propose une implémentation du **jeu de coloration de graphe** appliqué aux grilles bidimensionnelles finies.

Le jeu de coloration est un jeu combinatoire à deux joueurs (Alice et Bob) joué sur un graphe. Les joueurs colorient alternativement un sommet non coloré avec l’une des *k* couleurs disponibles, sous la contrainte qu’aucun sommet adjacent ne partage la même couleur.

- Alice gagne si tous les sommets sont colorés.
- Bob gagne s’il parvient à créer un sommet non coloriable (c’est-à-dire un sommet dont les voisins utilisent déjà toutes les k couleurs).

Cette implémentation se concentre sur les **grilles finies de taille m × n** et permet d’expérimenter différentes stratégies.

---

## Objectifs du projet

Ce projet a été réalisé dans le cadre d’un Master 2 en informatique.  
Il combine :

- Développement logiciel
- Validation expérimentale de stratégies connues
- Exploration de nouvelles pistes de recherche

Le logiciel permet :

- La visualisation interactive du jeu
- Le mode joueur contre joueur
- Le mode joueur contre ordinateur
- Le mode ordinateur contre ordinateur
- Le paramétrage de la taille de la grille
- Le choix du nombre de couleurs

---

## Stratégies implémentées

À ce jour, trois stratégies sont disponibles :

1. **Stratégie aléatoire**  
   Sélection d’un coup légal au hasard.

2. **Stratégie Bob pour les grilles 3×n avec 3 couleurs**  
   Implémentation d’une stratégie permettant à Bob de forcer un blocage.

3. **Début d’implémentation de la stratégie d’Alice pour les grilles 4×n**  
   Inclut la détection automatique des blocs et une logique partielle inspirée des résultats récents.

---

## Architecture du projet

Le projet suit une approche orientée objet structurée autour des composants suivants :

- `GameEngine` : gestion de la partie et des tours
- `Grid` : représentation de la grille
- `Cell` : représentation d’un sommet
- `Player` : abstraction d’un joueur
- `Strategy` : implémentation du design pattern Strategy
- Interface graphique : réalisée avec **Tkinter**

La structure de la grille est implémentée manuellement (sans bibliothèque externe de graphes), afin de permettre un contrôle précis pour la détection de configurations critiques et le développement de stratégies spécifiques.

---

## Lancement du programme

### Prérequis

- Python 3.x
- Tkinter (généralement inclus avec Python)
- Module `random` (bibliothèque standard)

### Exécution

```bash
python main.py