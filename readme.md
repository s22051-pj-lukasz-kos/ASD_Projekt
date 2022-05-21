# ASD Projekt

Porównanie czasów działania algorytmów na tablicach o losowych danych, posortowanych w kolejności rosnącej, posortowanej w kolejności malejącej.
Tablice zawierają 300k wpisów, każdy wpis to liczba z zakresu 0 - 65535 (0xFFFF)

## Tabela z wynikami

|               | Tablica losowych liczb | Tablica posortowanych liczb | Tablica odwrotnie posortowanych liczb |
| ------------- | ---------------------- | --------------------------- | ------------------------------------- |
| Heapsort      | 2,621s                 | 2,275s                      | 2,283s                                |
| Quicksort     | 0,858s                 | algorytm nie wykonał się    | algorytm nie wykonał się              |
| Merge Sort    | 1,970s                 | 1,665s                      | 1,606s                                |
| Counting Sort | 0,104s                 | 0,069s                      | 0,068s                                |

## Wnioski

### Heapsort

Heapsort jest wydajnym algorytmem, który wykazuje małe różnice między tabelami zawierającymi liczby losowe, a posortowane w dowolny sposób. Jednakże sortowanie przez kopcowanie jest nieznacznie szybsze (~15%) w przypadku posortowanych wartości.

### Quicksort

Szybkie sortowanie jest bardzo wydajnym algorytmem dla losowych danych, jednakże kompletnie nie radzi sobie z obliczaniem dużej ilości danych (>100k) posortowanych w jakikolwiek sposób. Kompilator przerywał działanie programu nie wywołując żadnego błędu, więc nie wiem dokładnie jaka jest przyczyna nieefektywności programu.

### Merge Sort

Algorytm wydajniejszy od sortowania przez kopcowanie i podobnie do niego lepiej sobie radzi z danymi już posortowanymi.

### Counting Sort

W metodzie sortowania przrez zliczanie zakładamy, że każdy z n elementów ciągu wejściowego jest liczbą całkowitą z przedziału od 0 do k.
Polega on na wykorzystaniu trzech tablic:

1. Tablicy danych wejściowych
2. Tablicy danych wyjściowych (zawierająca posortowane dane z tablicy 1)
3. Tablicy zliczającej, która zawiera ilość poszczególnych wartości z tablicy 1. Wartość elementu z tablicy 1 stanowi indeks elementu tablicy 3, a jego wartość określa ilość (powtarzalność).  
   Jest to ekstremalnie wydajny algorytm, jednakże posiada on dwa istotne wady:

- trzeba znać zakres danych tablicy (albo wyszukać je przy pomocy innych algorytmów),
- algorytm nie radzi sobie z zakresem znacznie przewyższającym ilość danych (np. dla zakresu 0 - 4 294 967 295, czyli 0xFFFFFFFF algorytm nie zakończył działania dla 300k wpisów).
  Z tego ostatniego wynika, że algorytm doskonale spisywałby się do sortowania powtarzalnych liczb.
  Dla powyższych danych (zakres 0 - 65535, 300k wpisów) sortowanie przez zliczanie okazał się być najbardziej wydajnym algorytmem ze wszystkich użytych.
