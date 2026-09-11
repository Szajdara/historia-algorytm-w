# Algorytm CART Drzewo decyzyjne
def decyzja_cart(wiek, dochod):
    if wiek < 30:
        return "Grupa A: Młody użytkownik"
    else:
        if dochod > 5000:
            return "Grupa B: Wysokie dochody"
        else:
            return "Grupa C: Standardowe dochody"

print("Test 1 (Wiek 25, Dochód 3000):")
print(decyzja_cart(25, 3000))
print("\nTest 2 (Wiek 42, Dochód 7500):")
print(decyzja_cart(42, 7500))