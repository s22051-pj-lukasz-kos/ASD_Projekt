# scalanie tablic
def merge(tab, p, q, r):
    # tworzymy lewą i prawą podtablicę
    n1 = q - p + 1
    n2 = r - q
    left = []
    right = []

    for i in range(0, n1): 
        left.append(tab[p + i])
    for j in range (0, n2):
        right.append(tab[q + 1 + j])

    # ustawiamy indeksy
    i = j = 0
    k = p

    # dopóki nie osiągniemy końca lewej bądź prawej podtablicy, 
    # mniejszą wartość umieszczamy w tab[k]
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else: 
            tab[k] = right[j]
            j += 1
        k += 1
    
    # po osiągnięciu końca lewej bądź prawej podtablicy
    # drugą tablicę dopinamy do końca tab
    while i < n1:
        tab[k] = left[i]
        i += 1
        k += 1
    
    while j < n2:
        tab[k] = right[j]
        j += 1
        k += 1

# sortowanie przez scalanie 
def merge_sort(tab, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(tab, p, q)
        merge_sort(tab, q + 1, r)
        merge(tab, p, q, r)