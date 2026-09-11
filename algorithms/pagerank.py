# Symulacja Algorytmu PageRank
pr = [0.333, 0.333, 0.333]
d = 0.85 # Współczynnik tłumienia

for i in range(1, 4):
    pr_nowy = [
        (1 - d) + d * (pr[2] / 2),
        (1 - d) + d * (pr[0] / 1 + pr[2] / 2),
        (1 - d) + d * (pr[1] / 1)
    ]
    pr = [round(x, 4) for x in pr_nowy]
    print(f"Iteracja {i} - PageRank stron [A, B, C]: {pr}")