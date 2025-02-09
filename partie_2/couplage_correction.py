"""
   ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
   Correction de la séance n°1 sur le couplage d'enregistrements.
    ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ . ~ .
"""

import string
import nltk

# --------------------
# ✏️ QUESTION 2


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


# --------------------
# ✏️ QUESTION 3


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


# --------------------
# ✏️ QUESTION 5


distance = nltk.edit_distance("martirs 4I", "Martyrs, 47")

# --------------------
# ✏️ QUESTION 6


def edit_distance_norm(champ1: str, champ2: str) -> float:
    distance_absolue = nltk.edit_distance(champ1, champ2)
    taille_plus_long_champ = max(len(champ1), len(champ2), 1)
    return distance_absolue / taille_plus_long_champ


# --------------------
# ✏️ QUESTION 7


def similarité_str(champ1: str, champ2: str) -> float:
    distance = edit_distance_norm(champ1, champ2)
    return 1.0 - distance


# --------------------
# ✏️ QUESTION 8


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


# --------------------
# ✏️ QUESTION 9


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


# --------------------
# ✏️ QUESTION 10


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
