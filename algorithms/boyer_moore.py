def boyer_moore(tekst, wzorzec):
    n, m = len(tekst), len(wzorzec)
    # Tablica przesunięć: zapamiętuje ostatni indeks każdego znaku we wzorcu
    bad_char = {char: i for i, char in enumerate(wzorzec)}

    s = 0  # Przesunięcie wzorca względem tekstu
    while s <= n - m:
        j = m - 1
        # Porównanie od prawej do lewej
        while j >= 0 and wzorzec[j] == tekst[s + j]:
            j -= 1

        if j < 0:
            return s  # Znaleziono wzorzec

        # Przeskok: wyrównaj niedopasowany znak lub przesuń o min. 1 pozycję
        s += max(1, j - bad_char.get(tekst[s + j], -1))

    return -1


# Przykład
tekst = "PROGRAMOWANIE ALGORYTMOW"
wzorzec = "RYM"
print("Indeks:", boyer_moore(tekst, wzorzec))