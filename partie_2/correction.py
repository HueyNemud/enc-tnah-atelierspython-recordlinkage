#!/usr/bin/env python
"""
   ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
   Correction de la séance n°2 sur le couplage d'enregistrements.
    ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
"""


import argparse
import csv
from util import print_couplage_tables, print_couplage

# Si vous avez renommé le fichier `couplage_correction.py`, ajustez l'import ci-dessous
# en conséquence.
from couplage_correction import couplage

# Déclaration des arguments de la ligne de commande
# - fichier1 : Table de données gauche
# - fichier2 : Table de données droit
# - sortie : Table de couplage CSV

cli_parser = argparse.ArgumentParser(
    description="Un utilitaire de couplage approximatif entre deux tables de données au format CSV."
)
cli_parser.add_argument(
    "fichier1", type=argparse.FileType("r"), help="Table de données gauche."
)
cli_parser.add_argument(
    "fichier2", type=argparse.FileType("r"), help="Table de données droit."
)
cli_parser.add_argument(
    "sortie", type=argparse.FileType("w"), help="Table de couplage CSV."
)

# On demande à argparse d'analyser les arguments de la ligne de commande
# La variable `args` contient les valeurs des arguments transmis par l'utilisateur
args = cli_parser.parse_args()

# 💡 Astuce **Python avancé, à petites doses**
#
# Pour séparer le premier élément d'une liste des autres, on peut utiliser la syntaxe suivante :
# premier, *reste = [1, 2, 3, 4, 5,...]
# Python va affecter le premier élément à la variable `premier`, et tout le reste à la variable `reste`
# ⚠️ Notez l'astérisque "*" devant la variable `reste` !
#       Il indique à Python que cette variable doit contenir tous les éléments restants de la liste.
#
# En plus, on utilise une *list comprehension* pour écrire une boucle *for* en une seule ligne.
# En combinant ces deux astuces, la ligne suivante lit les enregistrements du fichier CSV
#  et sépare l'entête des données...
# ...en une seule ligne de code ! Magique, non ?🪄
entête_1, *enregistrements_1 = [e for e in csv.reader(args.fichier1)]
entête_2, *enregistrements_2 = [e for e in csv.reader(args.fichier2)]


# On réalise le couplage des enregistrements
seuil = 0.5
couplages = couplage(enregistrements_1, enregistrements_2, seuil)

# Affichage du couplage
print("Couplage\n", "Paramètres", "seuil=", seuil)
for i, j, score in couplages:
    print(f"table_1[{i}] & table_2[{j}]", end=" ⇨ ")
    print_couplage(enregistrements_1[i], enregistrements_1[j], match=True, score=score)


# Affichage des tables couplées
print_couplage_tables(
    enregistrements_1,
    enregistrements_2,
    couplages,
    headers=["Index", *entête_1, "Match", "Score", "Index", *entête_2],
)

# Sauvegarde des couplages dans un fichier CSV
writer = csv.writer(args.sortie)
writer.writerow(["Index", *entête_1, "Score", "Index", *entête_2])
for i, j, score in couplages:
    writer.writerow([i, *enregistrements_1[i], score, j, *enregistrements_2[j]])
