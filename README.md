# Master TNAH - Atelier "Python pour les données de la recherche en histoire" - couplage d'enregistrements

Bienvenue sur le dépôt du matériel, code et instructions, pour  réaliser la première séquence de l'atelier "Python pour les données de la recherche en histoire" du master Technologies numériques appliquées à l'histoire à l'École Nationale des Chartes.

Cette première séquence est dédiée à la réalisation d'un **outil de couplage d'enregistrements** en ligne de commande.

Elle est composée de deux parties : 
1. Introduction au couplage d'enregistrements et réalisation d'un script Python dédié à cette tâche.
2. Création d'une interface en ligne de commande avec `argparse` pour coupler deux tables de données CSV.

Les deux séances s'appuient sur des données historiques réelles : les extractions des **annuaires du commerce de Paris au XIXe siècle** produites dans le projet de recherche [SODUCO](https://soduco.geohistoricaldata.org/) et diffusées sous license ouverte dans l'entrepôt de données NAKALA de [l'IR Huma-Num](https://www.huma-num.fr) : https://nakala.fr/collection/10.34847/nkl.abe0gxah.









Dernière mise à jour : **Février 2025**.


# Mise en place 🏗️



1. Télécharger le dépôt avec Git
```bash
git clone git@github.com:HueyNemud/enc-m2tnah-atelierspython-recordlinkage.git
```

2. Vérifier que Python 3.10 ou supérieur est utilisé
```bash
python --version
```

3. Au besoin, créez un nouvel environnement virtuel Python
```bash
python -m venv ~/python_atelierstnah
source ~/python_atelierstnah/bin/activate
```
