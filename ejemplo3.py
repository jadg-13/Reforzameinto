#Mostrar los numeros del 1 al 100 usando for

import os

try:
    os.system("cls || clear")
    os.system("color 0a")
    for i in range(1, 101):
        print(i)
except:
    print("Error inesperado")