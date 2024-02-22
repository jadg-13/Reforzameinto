#Dividir dos números
import os
try:
    os.system("cls || clear")
    os.system("color 0a")
    #leer los números
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    #dividir los números
    resultado = num1 / num2
    #mostrar el resultado
    os.system("color e4")
    print(f"El resultado de dividir {num1} entre {num2} es {resultado :.2f}")
#validar division por cero
except ZeroDivisionError:
    os.system("color c0")
    print("Error: No se puede dividir entre cero")
except:
    print("Error inesperado")