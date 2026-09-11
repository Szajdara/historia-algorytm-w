# Wyszukiwanie wzorca w tekście (Algorytm Boyera-Moorea)
def szukaj_wzorca(tekst, wzorzec):
    n = len(tekst)
    m = len(wzorzec)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and tekst[i + j] == wzorzec[j]:
            j -= 1
        if j < 0:
            return i
        i += 1
    return -1

tekst = "PROGRAMOWANIE ALGORYTMOW"
wzorzec = "RYM"
indeks = szukaj_wzorca(tekst, wzorzec)
print(f"Tekst: '{tekst}'")
print(f"Szukany wzorzec: '{wzorzec}'")
print(f"Znaleziono na indeksie: {indeks}")