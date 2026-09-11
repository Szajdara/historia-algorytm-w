def dijkstra(graf, start, koniec):
    odleglosci = {wezel: float('inf') for wezel in graf}
    odleglosci[start] = 0
    kolejka = [(0, start)]
    
    while kolejka:
        # Znajdujemy i usuwamy element o najmniejszym koszcie
        kolejka.sort(key=lambda x: x[0])
        aktualny_koszt, aktualny = kolejka.pop(0)
        
        if aktualny == koniec:
            return aktualny_koszt
            
        if aktualny_koszt > odleglosci[aktualny]:
            continue
            
        for sasiad, waga in graf[aktualny].items():
            koszt = aktualny_koszt + waga
            if koszt < odleglosci[sasiad]:
                odleglosci[sasiad] = koszt
                kolejka.append((koszt, sasiad))
                
    return odleglosci[koniec]

# Przykład użycia:
graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

print("Najkrótszy koszt:", dijkstra(graf, 'A', 'E'))