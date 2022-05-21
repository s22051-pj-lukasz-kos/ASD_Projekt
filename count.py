# Sortowanie przez zliczanie (counting sort)
# W metodzie sortowania przez zliczanie zakładamy, 
# że każdy z n elementów ciągu wejściowego jest liczbą całkowitą z przedziału od 0 do k.
# tab_a tablica danych wejściowych, 
# tab_b tablica posortowanych danych wejściowych
def counting_sort(tab_a, k): 
    # tablica na tymczasowe dane pomocnicze
    tab_c = []
    for i in range(k + 1):
        tab_c.append(0)

    # zliczanie poszczególnych wartości z tab_a
    for j in tab_a:
        tab_c[j] += 1

    # zsumuj wartość komórki z wartością z poprzedniej komórki
    for i in range(1, k + 1):
        tab_c[i] += tab_c[i - 1]
    
    # oblicz pozycję elementów
    tab_b = [0] * len(tab_a)
    
    # posortuj tablicę
    for j in range(len(tab_a) - 1, -1, -1):
        currentEl = tab_a[j]
        tab_c[currentEl] -= 1
        newPosition = tab_c[currentEl]
        tab_b[newPosition] = currentEl
    
    return tab_b
