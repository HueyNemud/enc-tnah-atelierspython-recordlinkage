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
    max_text_len: int = 25,
):
    from tabulate import tabulate  # pip install tabulate
    import textwrap

    # Tronque les longues chaînes de caractères pour l'affichage
    _tbl1 = [
        [textwrap.shorten(cell, width=max_text_len) for cell in row] for row in table_1
    ]
    _tbl2 = [
        [textwrap.shorten(cell, width=max_text_len) for cell in row] for row in table_2
    ]

    # Optimisation : dictionnaire des couplages T1->T2 et T2->T1
    cp_12 = {i: [] for i in range(len(_tbl1))}
    cp_21 = {i: [] for i in range(len(_tbl2))}
    for i, j, s in couplages:
        cp_12[i].append((j, s))
        cp_21[j].append((i, s))

    rows = []
    for i, e in enumerate(_tbl1):
        if cp_12[i]:
            for j, s in cp_12[i]:
                rows.append([i] + e + ["✅", s, j] + _tbl2[j])
        else:
            rows.append([i] + e + ["⛔"])

    for j, e in enumerate(_tbl2):
        if not cp_21[j]:
            rows.append([""] + [""] * len(_tbl1[0]) + ["⛔", None, j] + e)

    table = tabulate(rows, headers, tablefmt="outline", floatfmt=".2f")
    print(table)
