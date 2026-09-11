# Szybkie sortowanie (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lewe = [x for x in arr if x < pivot]
    srodek = [x for x in arr if x == pivot]
    prawe = [x for x in arr if x > pivot]
    return quick_sort(lewe) + srodek + quick_sort(prawe)

liczby = [29, 10, 14, 37, 13, 9, 21]
print(f"Przed sortowaniem: {liczby}")
print(f"Po sortowaniu: {quick_sort(liczby)}")