def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partycjonowanie (Lomuto)
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        # Umieszczenie pivota na właściwym miejscu
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        # Rekurencja musi być WEWNĄTRZ bloku 'if low < high'
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

    return arr

dane = [29, 10, 14, 37, 13, 9, 21]
print("Przed:", dane)
quick_sort_inplace(dane)
print("Po:", dane)