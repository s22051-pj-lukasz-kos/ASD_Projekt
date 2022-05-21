import random

#Generuje tablicę i plik zmiennych liczb
tablica_rand = []


for i in range(300000):
    x = random.randint(0,65535)
    tablica_rand.append(x)

with open("tablicaRandomowa.txt", "w") as file:
    file.write('\n'.join(str(number) for number in tablica_rand))

#Generuje tablicę i plik posortowanych liczb
tablica_rand.sort()
with open("tablicaPosortowana.txt", "w") as file:
    file.write('\n'.join(str(number) for number in tablica_rand))
    

#Generuje tablicę i plik odwrotnie posortowanych liczb
tablica_rand.sort(reverse=True)
with open("tablicaOdwrotniePosortowana.txt", "w") as file:
    file.write('\n'.join(str(number) for number in tablica_rand))