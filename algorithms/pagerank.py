def pagerank(graf_linkow, d=0.85, iteracje=3):
    N = len(graf_linkow)
    pr = [1.0 / N] * N
    
    # Obliczamy ile linków wychodzi z każdej strony
    wychodzace = [sum(row) for row in graf_linkow]

    for krok in range(1, iteracje + 1):
        pr_nowy = [0.0] * N
        for i in range(N):
            suma_wplywow = 0.0
            for j in range(N):
                # Jeśli strona j linkuje do strony i
                if graf_linkow[j][i] == 1:
                    suma_wplywow += pr[j] / wychodzace[j]
            
            pr_nowy[i] = (1 - d) / N + d * suma_wplywow
            
        pr = [round(x, 4) for x in pr_nowy]
        print(f"Iteracja {krok} - PageRank [A, B, C]: {pr}")

# Graf: row = z kogo wychodzi, col = do kogo idzie
# A -> B, C | B -> C | C -> A, B
graf = [
    [0, 1, 1],  # Strona A
    [0, 0, 1],  # Strona B
    [1, 1, 0]   # Strona C
]

pagerank(graf)