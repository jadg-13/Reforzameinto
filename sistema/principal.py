import clases as c
import os 

bodegas = c.Bodega()

def ingresarProducto():
    try:
        os.system("cls || clear")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        producto = c.Producto(nombre, precio, cantidad)
        bodegas.agregar_producto(producto)
    except:
        print("Error inesperado")

def menu():
    while True:
        os.system("cls || clear")
        print("Cantidad de productos: " , str(len(bodegas.productos)))
        print("1. Ingresar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                ingresarProducto()
            elif opcion == 2:
                print("ver productos")
                bodegas.mostrar_productos()
                os.system("pause")
            elif opcion == 3:
                break
            else:
                print("Opción no válida")
        except:
            print("Error: Ingrese un número entero")

def main():
    menu()

if __name__ == "__main__":
    main()