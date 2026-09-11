# Algorytm Dijkstry
graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

def dijkstra(start, koniec):
    odleglosci = {wezel: float('inf') for wezel in graf}
    odleglosci[start] = 0
    odwiedzone = set()
    
    while len(odwiedzone) < len(graf):
        nieodwiedzone = [w for w in graf if w not in odwiedzone]
        if not nieodwiedzone:
            break
        aktualny = min(nieodwiedzone, key=lambda w: odleglosci[w])
        
        if odleglosci[aktualny] == float('inf'):
            break
        odwiedzone.add(aktualny)
        
        for sasiad, waga in graf[aktualny].items():
            koszt = odleglosci[aktualny] + waga
            if koszt < odleglosci[sasiad]:
                odleglosci[sasiad] = koszt
                
    return odleglosci[koniec]

koszt = dijkstra('A', 'E')
print(f"Najkrótszy koszt przejazdu z A do E: {koszt}")