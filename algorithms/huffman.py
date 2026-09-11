def kodowanie_huffmana(tekst):
    if not tekst:
        return {}

    czestotliwosc = {}
    for znak in tekst:
        czestotliwosc[znak] = czestotliwosc.get(znak, 0) + 1

    # Przypadek brzegowy: tylko 1 unikalny znak w tekście
    if len(czestotliwosc) == 1:
        char = list(czestotliwosc.keys())[0]
        return {char: "0"}

    # Format węzła: [waga, [znak, kod], [znak, kod], ...]
    wezly = [[freq, [char, ""]] for char, freq in czestotliwosc.items()]

    while len(wezly) > 1:
        wezly.sort(key=lambda x: x[0])
        lewy = wezly.pop(0)
        prawy = wezly.pop(0)

        # Dopisywanie '0' dla lewego poddrzewa i '1' dla prawego
        for item in lewy[1:]:
            item[1] = '0' + item[1]
        for item in prawy[1:]:
            item[1] = '1' + item[1]

        nowy_wezel = [lewy[0] + prawy[0]] + lewy[1:] + prawy[1:]
        wezly.append(nowy_wezel)

    # Zwracamy słownik dla łatwiejszego odczytu {znak: kod}
    return dict(wezly[0][1:])

# --- Test ---
tekst = "algorytmy"
kody = kodowanie_huffmana(tekst)

print("Tekst:", tekst)
print("Kody Huffmana:")
for char, kod in kody.items():
    print(f"  '{char}': {kod}")