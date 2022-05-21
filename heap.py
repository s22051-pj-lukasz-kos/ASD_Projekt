# przywracanie własności kopca
def max_heapify(tab, index, heapsize):
    left = 2 * index 
    right = 2 * index + 1
    largest = index

    if left < heapsize and tab[left] > tab[largest]:
        largest = left
    
    if right < heapsize and tab[right] > tab[largest]:
        largest = right
    
    if largest != index:
        tab[index], tab[largest] = tab[largest], tab[index]
        max_heapify(tab, largest, heapsize)

# budowanie kopca typu max
def build_max_heap(tab, heapsize):
    start = (len(tab) // 2) - 1
    for index in range(start, -1, -1):
        max_heapify(tab, index, heapsize)

# sortowanie przez kopcowanie
def heapsort(tab):
    heapsize = len(tab)
    build_max_heap(tab, heapsize)
    for index in range(len(tab) - 1, 0, -1):
        tab[0], tab[index] = tab[index], tab[0]
        heapsize -= 1
        max_heapify(tab, 0, heapsize)
