# Algorytm A*
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start = (0, 0)
cel = (3, 3)
pozycja_aktualna = (1, 2)

g_score = 3
h_score = manhattan(pozycja_aktualna, cel)
f_score = g_score + h_score

print(f"Pozycja: {pozycja_aktualna}, Cel: {cel}")
print(f"g(n) [koszt dotychczasowy] = {g_score}")
print(f"h(n) [heurystyka do celu] = {h_score}")
print(f"f(n) = g(n) + h(n) = {f_score}")    