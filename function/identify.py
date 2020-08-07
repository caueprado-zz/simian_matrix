import json
import numpy as np
import re
import timeit

patterns = ("A{4}", "T{4}", "G{4}", "C{4}")


def verify(dna):
    jload = json.loads(dna)
    s_min = len(jload["dna"])
    if s_min < 4:
        raise Exception("Invalid matrix size")

    ##Constante para evitar a leitura das diagonais com tamanho menor que quatro
    q_diags = s_min - 3

    normal_m = []

    for row in jload["dna"]:
        column = []
        for letter in row:
            if letter != "A" and letter != "G" and letter != "C" and letter != "T":
                raise Exception("Invalid aminoacid chain")
            column.append(letter)
        normal_m.append(column)

    t_matrix = np.transpose(normal_m)
    primary_diagonals = get_diagonal(normal_m, 0, q_diags, 1)
    primary_diagonals.extend(get_diagonal(normal_m, 1, q_diags, -1))

    secondary_diagonals = get_diagonal(np.fliplr(normal_m), 0, q_diags, 1)
    secondary_diagonals.extend(get_diagonal(np.fliplr(normal_m), 1, q_diags, -1))

    possibilities = [normal_m, t_matrix, primary_diagonals, secondary_diagonals]
    return is_simian(possibilities, s_min)


def find_gene(gene):
    for pattern in patterns:
        match = re.search(pattern, gene)
        if type(match) == re.Match:
            return True
    return False


def get_diagonal(matrix, start, end, side):
    l_diagonals = []
    for d in range(start, end):
        l_diagonals.append(np.diag(matrix, k=side*d))
    return l_diagonals


def is_simian(possibilities, s_min):
    for s in range(s_min):
        for sequence in possibilities:
            try:
                if len(sequence) > s:
                    join = "".join(sequence[s])
                    if find_gene(join):
                        return True
            except ValueError:
                print("error")
    return False
