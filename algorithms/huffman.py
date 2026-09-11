# Kodowanie Huffmana
def kodowanie_huffmana(tekst):
    czestotliwosc = {}
    for znak in tekst:
        czestotliwosc[znak] = czestotliwosc.get(znak, 0) + 1
        
    wezly = [[freq, [char, ""]] for char, freq in czestotliwosc.items()]
    
    while len(wezly) > 1:
        wezly.sort(key=lambda x: x[0])
        lewy = wezly.pop(0)
        prawy = wezly.pop(0)
        
        for item in lewy[1:]:
            item[1] = '0' + item[1]
        for item in prawy[1:]:
            item[1] = '1' + item[1]
            
        nowy_wezel = [lewy[0] + prawy[0]] + lewy[1:] + prawy[1:]
        wezly.append(nowy_wezel)
        
    return wezly[0][1:]

tekst = "algorytmy"
print(f"Tekst źródłowy: {tekst}")
kody = kodowanie_huffmana(tekst)
print("Wygenerowane kody Huffmana:")
for symbol, kod in kody:
    print(f"'{symbol}' : {kod}")