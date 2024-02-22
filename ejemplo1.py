#Convertir metros a centimetros
import os

os.system("cls || clear")
os.system("color 0a")
#leer la cantidad en metros
metros = float(input("Cantidad de metros: "))

#formula para convertir metros a centimetros
centimetros = metros * 100

#mostrar el resultado
os.system("color e4")
print(f"{metros} metros equivalen a {centimetros} centimetros")
