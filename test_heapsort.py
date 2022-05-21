import heap
import sys
import time
import gc

# ustawianie limitu rekursji
sys.setrecursionlimit(500000)

# importowanie danych do 3 różnych tablic
# tablica danych losowych 
tablica_randomowa = []
with open("tablicaRandomowa.txt", "r") as file_random:
    for number in file_random.readlines():
        tablica_randomowa.append(int(number))

# tablica danych posortowanych 
tablica_posortowana = []
with open("tablicaPosortowana.txt", "r") as file_sort:
    for number in file_sort.readlines():
        tablica_posortowana.append(int(number))

# tablica danych odwrotnie posortowanych 
tablica_odwrotnie_posortowana = []
with open("tablicaPosortowana.txt", "r") as file_rev_sort:
    for number in file_rev_sort.readlines():
        tablica_odwrotnie_posortowana.append(int(number))


# HEAP SORT
# testowanie czasu działania sortowania przez kopcowanie dla danych losowych
start_time_heap_random = time.time()
heap.heapsort(tablica_randomowa)
print("Heapsort dla losowych liczb zajmuje %.3fs" % (time.time() - start_time_heap_random))

# testowanie czasu działania sortowania przez kopcowanie dla danych uporządkowanych rosnąco
start_time_heap_sort = time.time()
heap.heapsort(tablica_posortowana)
print("Heapsort dla liczb ułożonych rosnąco zajmuje %.3fs" % (time.time() - start_time_heap_sort))

# testowanie czasu działania sortowania przez kopcowanie dla danych uporządkowanych malejąco
start_time_heap_rev_sort = time.time()
heap.heapsort(tablica_odwrotnie_posortowana)
print("Heapsort dla liczb ułożonych malejąco zajmuje %.3fs" % (time.time() - start_time_heap_rev_sort))

# zwalnianie pamięci
del tablica_randomowa, tablica_posortowana, tablica_odwrotnie_posortowana
del start_time_heap_random, start_time_heap_sort, start_time_heap_rev_sort
gc.collect()