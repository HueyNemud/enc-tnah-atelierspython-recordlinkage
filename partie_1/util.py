"""Fontion utilitaires d'affichage dans la console."""


def print_couplage(
    enregistrement_1: list[str],
    enregistrement_2: list[str],
    match: bool = None,
    score: float = None,
):
    """Affiche un couplage entre deux enregistrements."""
    pattern = "{match} {score} :: {pairs}"
    match = "✅ MATCH" if match else "⛔ NON MATCH"
    score = f"({score:.2f})" if score else ""
    pairs = " • ".join(f"{pair}" for pair in zip(enregistrement_1, enregistrement_2))
    print(pattern.format(match=match, score=score, pairs=pairs))


def q(question: int):
    """Affiche le numéro de la question."""
    print(f"\n✏️ QUESTION {question}\n---")


def print_couplage_tables(
    table_1: list[list],
    table_2: list[list],
    couplages: list[tuple],
    headers: list[str] = [],
):
    from tabulate import tabulate  # pip install tabulate

    # Optimisation : dictionnaire des couplages T1->T2 et T2->T1
    cp_12 = {i: [] for i in range(len(table_1))}
    cp_21 = {i: [] for i in range(len(table_2))}
    for i, j, s in couplages:
        cp_12[i].append((j, s))
        cp_21[j].append((i, s))

    rows = []
    for i, e in enumerate(table_1):
        if cp_12[i]:
            for j, s in cp_12[i]:
                rows.append([i] + e + ["✅", s, j] + table_2[j])
        else:
            rows.append([i] + e + ["⛔"])

    for j, e in enumerate(table_2):
        if not cp_21[j]:
            rows.append([""] + [""] * len(table_1[0]) + ["⛔", None, j] + e)

    print(tabulate(rows, headers, tablefmt="outline", floatfmt=".2f"))
