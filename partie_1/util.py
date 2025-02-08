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


def print_couplage_tables(table_1, table_2, couplages, headers=[]):
    """Affiche les deux tables avec les couplages mis en évidence.
    Nécessite tabulate."""

    from tabulate import tabulate  # pip install tabulate

    nlines = len(table_1) + len(table_2) - len(couplages)
    join_table = [[] for _ in range(nlines)]

    for i, e in enumerate(table_1):
        join_table[i] = e + ["⛔", None]

    for i, j, score in couplages:
        join_table[i] = table_1[i] + ["✅"] + [score] + table_2[j]

    t2_coupled = [j for _, j, _ in couplages]
    r = len(table_1)
    for j, e in enumerate(table_2):
        if j not in t2_coupled:
            join_table[r] = [""] * len(table_1[0]) + ["⛔", None] + e
            r += 1

    print(tabulate(join_table, headers, tablefmt="outline", floatfmt=".2f"))
