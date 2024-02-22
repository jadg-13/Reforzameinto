# Leer la edad de una persona y decir si puede votor o no
import os

os.system("cls || clear")
try:
    #leer la edad
    edad = int(input("Edad: "))
    if edad >= 16:
        print("Puede votar")
    else:
        print("No puede votar")
except:
    print("Error: Ingrese un número entero")
    