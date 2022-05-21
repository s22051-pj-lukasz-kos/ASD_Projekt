import count
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

# COUNTING SORT
# testowanie czasu działania sortowania przez zliczanie dla danych losowych
start_time_count_random = time.time()
table = []
table = count.counting_sort(tablica_randomowa, 65535)
print("Counting sort dla losowych liczb zajmuje %.3fs" % (time.time() - start_time_count_random))

# testowanie czasu działania sortowania przez zliczanie dla danych uporządkowanych rosnąco
start_time_count_sort = time.time()
count.counting_sort(tablica_posortowana, 65535)
print("Counting sort dla liczb ułożonych rosnąco zajmuje %.3fs" % (time.time() - start_time_count_sort))

# testowanie czasu działania sortowania przez zliczanie dla danych uporządkowanych malejąco
start_time_count_rev_sort = time.time()
count.counting_sort(tablica_odwrotnie_posortowana, 65535)
print("Counting sort dla liczb ułożonych malejąco zajmuje %.3fs" % (time.time() - start_time_count_rev_sort))

# zwalnianie pamięci
del tablica_randomowa, tablica_posortowana, tablica_odwrotnie_posortowana
del start_time_count_random, start_time_count_sort, start_time_count_rev_sort
gc.collect()