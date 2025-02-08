"""
   ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
   Correction de la séance n°1 sur le couplage d'enregistrements.
    ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
"""

import string
import nltk

# Fontion utilitaires locales
from util import print_couplage, q, print_couplage_tables

# --------------------
# ✏️ QUESTION 2
q(2)

#  1) Complétez la fonction `calculer_score_exact(list[str], list[str])` pour que :
# - elle prenne en paramètre deux listes de chaînes de caractères
# - elle renvoie 1 si les éléments des deux listes sont identiques deux à deux, 0 sinon.

# 2) Completez la fonction `couplage_exact(list[str], list[str])` qui :
# - prend en paramètre deux enregistrements représentés par des listes de chaînes de caractères ;
# - retourne un booléen indiquant si les deux enregistrements sont couplés.

# 3) Testez la méthode avec les deux enregistrements ci-dessous.

# 💡 Astuces :
# Notez l'utilisation d'annotations de type pour les paramètres (list[str]) et le retour (int) de la fonction.
# C'est une pratique TRÈS recommandée pour améliorer la lisibilité et la maintenance du code.


def calculer_score_exact(
    enregistrement_1: list[str], enregistrement_2: list[str]
) -> int:
    # 🏗️ À COMPLÉTER
    for i in range(len(enregistrement_1)):
        if enregistrement_1[i] != enregistrement_2[i]:
            return 0
    return 1
    # On aurait aussi écrire plus simplement :
    #  return int(enregistrement_1 == enregistrement_2)


def couplage_exact(enregistrement_1: list[str], enregistrement_2: list[str]) -> bool:
    # 🏗️ À COMPLÉTER
    score = calculer_score_exact(enregistrement_1, enregistrement_2)
    return score == 1


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

enregistrement_1 = ["Duchesne", "peintre-vitrier", "Amboise, 9"]
enregistrement_2 = ["Duchesne", "peintre-vitrier", "Amboise, 9"]

match = couplage_exact(enregistrement_1, enregistrement_2)

print_couplage(enregistrement_1, enregistrement_2, match)


# --------------------
# ✏️ QUESTION 3
q(3)

# 1) Complétez la fonction `normalisation(str)` qui :
#  - prend en paramètre la valeur d'un champ (une chaîne de caractères) ;
#  - renvoie la chaîne de caractères normalisée

# 2) Appliquez la fonction de normalisation aux deux enregistrements ci-dessous
# et testez le couplage exact avec les champs normalisés.

# 💡 Astuces :
#  1] La méthode str.lower() renvoie une copie de la chaîne de caractères en minuscules.
# Exemple : "Bonjour".lower() renvoie "bonjour".

#  2] La méthode str.translate() permet de remplacer une liste de caractères par une autre.
# Pour utiliser cette méthode, voir : https://waytolearnx.com/2020/07/python-la-methode-string-translate.html
# Exemple : "Bonjour".translate(str.maketrans("o", "*")) renvoie "B*nj*ur".

#  3] Le 3e paramètre de la méthode str.maketrans() permet de spécifier les caractères à supprimer.
# Voir : https://www.w3schools.com/python/ref_string_maketrans.asp
# Exemple : "Bonjour".translate(str.maketrans("o", "*", "j")) renvoie "B*n*ur".

# 4 La constante string.punctuation (du module string, à importer) contient la liste des caractères de ponctuation.

#  4] La méthode str.strip() permet de supprimer les espaces en début et fin de chaîne.


def normaliser_champ(champ: str) -> str:
    # 🏗️ À COMPLÉTER
    # 1. Tout mettre en minuscule
    normalisé = champ.lower()
    # 2. Remplacer les caractères accentués par leur équivalent non accentué
    # On utilise aussi maketrans pour supprimer la ponctuation
    translation_table = str.maketrans(
        "éèêëàâäôöûüùçïî", "eeeeaaaoouuucii", string.punctuation
    )
    normalisé = normalisé.translate(translation_table)
    # 3. Supprimer les espaces inutiles en début et fin de chaîne
    normalisé = normalisé.strip()
    return normalisé


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

enregistrement_1 = ["duchesne,,", "peintre vÎtrier", "amboise 9"]
enregistrement_2 = ["DUchësne", "Peintre -Vitrier", "Amboise, 9."]

e1 = [normaliser_champ(c) for c in enregistrement_1]
e2 = [normaliser_champ(c) for c in enregistrement_2]

match = couplage_exact(e1, e2)

print_couplage(enregistrement_1, enregistrement_2, match)

# --------------------
# ✏️ QUESTION 5
q(5)

distance = nltk.edit_distance("martirs 4I", "Martyrs, 47")

# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

print("nltk.edit_distance('martirs 4I, 'Martyrs, 47') =", distance)

# 💡 Astuce :  le mot-clé assert vérifie qu'une condition est vraie,
#  sinon une exception AssertionError est levée.
# On utilise assert essentiellement pour des tests durant le développement,
# mais pas dans le code en production.
assert distance == 4

# --------------------
# ✏️ QUESTION 6
q(6)


def edit_distance_norm(champ1: str, champ2: str) -> float:
    distance_absolue = nltk.edit_distance(champ1, champ2)
    taille_plus_long_champ = max(len(champ1), len(champ2), 1)
    return distance_absolue / taille_plus_long_champ


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

s1 = "martirs 4I"
s2 = "Martyrs, 47"
distance_norm = edit_distance_norm(s1, s2)
print(f"edit_distance_norm('{s1}', '{s2}') = {distance_norm:.2f}")

# 💡 Astuce :  notez le formatage du nombre flottant distance_norm avec
# la syntaxe f"{distance_norm:.2f}".
# L'ajout de ":.2f" permet d'afficher le nombre avec deux chiffres après la virgule.
# Il existe de nombreuses options de formatage, voir : https://pyformat.info/

# --------------------
# ✏️ QUESTION 7
q(7)


def similarité_str(champ1: str, champ2: str) -> float:
    distance = edit_distance_norm(champ1, champ2)
    return 1.0 - distance


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

s1 = "martirs 4I"
s2 = "Martyrs, 47"
sim = similarité_str(s1, s2)
print(f"similarité_str('{s1}', '{s2}') = {sim:.2f}")


# --------------------
# ✏️ QUESTION 8
q(8)

# 💡 Astuce

# 1] Par simplicité, considérez que les deux enregistrements
# ont **le même nombre de champs**, ie. les listes ont la même longueur.

#  2] Pour itérer sur deux listes en parallèle, on peut utiliser la fonction zip(liste1, liste2).
# Elle renvoie un itérateur qui combine les éléments des deux listes sous forme de tuples.

# 3] La racine n-ième d'un nombre x est égale à x^(1/n).
# En Python, on peut calculer la racine n-ième d'un nombre x avec l'opérateur **.
# Exemple : 8**(1/3) renvoie la racine cubique de 8.


def calculer_score_approximatif(
    enregistrement_1: list[str], enregistrement_2: list[str], alpha: float = 1.0
) -> float:

    # ⚠️ On suppose que les deux enregistrements ont le même nombre de champs
    nombre_champs = len(enregistrement_1)

    # Calcul du produit des similarités entre les champs
    produit_des_similarités = 1.0
    for champ1, champ2 in zip(enregistrement_1, enregistrement_2):
        sim = similarité_str(champ1, champ2)
        sim = sim**alpha  # Pondération de la similarité, voir l'encart "Bonus"
        produit_des_similarités *= sim

    # Calcul et renvoi de la moyenne géométrique
    moyenne_géométrique = produit_des_similarités ** (1 / nombre_champs)
    return moyenne_géométrique


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

lacroix_1841 = [
    "lacrox (paul, (bibliophile iaco",
    "membre du coniite des chartes",
    "martirs 4I",
]
lacroix_1844 = [
    "Lacroix Paul. (Bibliophile jacob",
    "membre du com. des chartes",
    "Martyrs, 47",
]

score = calculer_score_approximatif(lacroix_1841, lacroix_1844)

print(
    "Similarité entre les enregistrements lacroix_1841 et lacroix_1844 :",
    f"{score:.2f}",
)


# --------------------
# ✏️ QUESTION 9
q(9)


def couplage_approximatif(
    enregistrement_1: list[str],
    enregistrement_2: list[str],
    seuil: float = 0.8,
    alpha: float = 1.0,
) -> bool:
    # Normalise le score pour qu'il soit compris entre 0 et 1
    seuil = min(max(seuil, 0.0), 1.0)

    # Normalise les champs des deux enregistrements
    norm_1 = [normaliser_champ(c) for c in enregistrement_1]
    norm_2 = [normaliser_champ(c) for c in enregistrement_2]

    # Calcule le score approximatif entre les deux enregistrements
    score = calculer_score_approximatif(norm_1, norm_2, alpha)

    # Décide si les enregistrements sont couplés
    match = score >= seuil
    return match, score


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

seuil = 0.5

print("Couplage\n", "Paramètres", "seuil=", seuil)

lanet_a = ["Lanet (Mme J.-A", 'professeur d" "harmonie', "Beaux-Arts 6"]
lanet_b = ["Lanet (Mme)", 'professeur d" "harmonic', "Beaux-Arts"]

couplage, score = couplage_approximatif(lanet_a, lanet_b, seuil)
print_couplage(lanet_a, lanet_b, couplage, score)

laplace_a = ["Laplace et Dumont (Mlles", "institutrices", "Lions-St-Paul 14"]
laplace_b = ["Laplace et Dumont (Mlles)", "institutrices", "Lions-St-Paul 14"]

couplage, score = couplage_approximatif(laplace_a, laplace_b, seuil)
print_couplage(laplace_a, laplace_b, couplage, score)

regnault_a = ["Regnault et vue Poupinel", "fab. d" "ouates, depět", "47 Cha-ronne"]
regnault_b = ["Regnault et Vve Poupinel", "fab. d" "ouates, depet", "Charonne 47"]

couplage, score = couplage_approximatif(regnault_a, regnault_b, seuil)
print_couplage(regnault_a, regnault_b, couplage, score)

dasté_a = ["Dasté", "menuisier-ébèniste", "Notre-Dame, 27"]
dasté_b = ["Dasté (J.)", "menuisier", "Regard, 5"]

couplage, score = couplage_approximatif(dasté_a, dasté_b, seuil)
print_couplage(dasté_a, dasté_b, couplage, score)

dasté_a = ["Goix (Mme.)", "dentelière", "c. de Tourny, 56"]
dasté_b = ["Goix", "dentelle et articles fëm.", "Tourny S6"]

couplage, score = couplage_approximatif(dasté_a, dasté_b, seuil)
print_couplage(dasté_a, dasté_b, couplage, score)


# --------------------
# ✏️ QUESTION 10
q(10)

# 💡 Astuce : pour connaitre l'index de l'élément courant lorsqu'on itère
# sur une liste, on peut utiliser la fonction enumerate(liste) ainsi :
# for index, element in enumerate(liste):
#     ...


def couplage(
    table_1: list[list[str]],
    table_2: list[list[str]],
    seuil: float = 0.8,
    alpha: float = 1.0,
) -> list[tuple[int, int]]:
    # Cette liste va contenir les indices des enregistrements couplés, avec leur score.
    liste_couplages = []

    for i, enregistrement_1 in enumerate(table_1):
        for j, enregistrement_2 in enumerate(table_2):
            match, score = couplage_approximatif(
                enregistrement_1, enregistrement_2, seuil, alpha
            )
            if match:
                liste_couplages.append((i, j, score))
    return liste_couplages


# 🧪  VALIDATION 🧪
# Décommentez les lignes suivantes et exécutez le code pour tester votre fonction.

table_1 = [
    ["Dasté", "menuisier-ébèniste", "Notre-Dame, 27"],
    ["Loze (Jean)", "potier d'etain", "Greneta l2"],
    ["Lanet (Mme J.-A", 'professeur d" "harmonie', "Beaux-Arts 6"],
    ["Laplace et Dumont (Mlles", "institutrices", "Lions-St-Paul 14"],
    ["Regnault et vue Poupinel", "fab. d" "ouates, depět", "47 Cha-ronne"],
]

table_2 = [
    ["Dasté (J.)", "menuisier", "Regard, 5"],
    ["Lanet (Mme)", 'professeur d" "harmonic', "Beaux-Arts"],
    ["Laplace et Dumont (Mlles)", "institutrices", "Lions-St-Paul 14"],
    ["Regnault et Vve Poupinel", "fab. d" "ouates, depet", "Charonne 47"],
    ["Weill (S.) jeune", "négociant", "St.-Dominique, 18"],
]

seuil = 0.3
alpha = 1.0

couplages = couplage(table_1, table_2, seuil, alpha)

print("Couplage\n", "Paramètres", "seuil=", seuil, "alpha=", alpha)

for i, j, score in couplages:
    print(f"table_1[{i}] & table_2[{j}]", end=" ⇨ ")
    print_couplage(table_1[i], table_2[j], match=True, score=score)


# 🧪  BONUS 🧪
# ⚠️ Pour que la fonction print_couplage_tables fonctionne,
#  vous devez installer le module tabulate : pip install tabulate
print_couplage_tables(
    table_1,
    table_2,
    couplages,
    headers=[
        "1.ligne",
        "1.PER",
        "1.ACT",
        "1.LOC",
        "Match",
        "Score",
        "2.ligne",
        "2.PER",
        "2.ACT",
        "2.LOC",
    ],
)
