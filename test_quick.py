import quick
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
with open("tablicaOdwrotniePosortowana.txt", "r") as file_rev_sort:
    for number in file_rev_sort.readlines():
        tablica_odwrotnie_posortowana.append(int(number))


# QUICK SORT
# testowanie czasu działania szybkiego sortowania dla danych losowych
start_time_quick_random = time.time()
quick.quicksort(tablica_randomowa, 0, len(tablica_randomowa) - 1)
print("Quicksort dla losowych liczb zajmuje %.3fs" % (time.time() - start_time_quick_random))

# testowanie czasu działania szybkiego sortowania dla danych uporządkowanych rosnąco
# NOTE: dla danych posortowanych (zarówno rosnąco jak i malejąco) Quicksort wg Lomuto nie radzi sobie z dużą ilością danych > 100k
start_time_quick_sort = time.time()
quick.quicksort(tablica_posortowana, 0, len(tablica_posortowana) - 1)
print("Quicksort dla liczb ułożonych rosnąco zajmuje %.3fs" % (time.time() - start_time_quick_sort))

# testowanie czasu działania szybkiego sortowania dla danych uporządkowanych malejąco
start_time_quick_rev_sort = time.time()
quick.quicksort(tablica_odwrotnie_posortowana, 0, len(tablica_odwrotnie_posortowana) - 1)
print("Quicksort dla liczb ułożonych malejąco zajmuje %.3fs" % (time.time() - start_time_quick_rev_sort))

# zwalnianie pamięci
del tablica_randomowa, tablica_posortowana, tablica_odwrotnie_posortowana
del start_time_quick_random, start_time_quick_sort, start_time_quick_rev_sort
gc.collect()