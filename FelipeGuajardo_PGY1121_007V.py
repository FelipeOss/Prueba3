import numpy as np

matrizLote = [[' ' for _ in range(5)] for _ in range(4)]

lotes = [
    {'numero': '1', 'tamaño': '5000 m2', 'precio': '$300,000'},
    {'numero': '2', 'tamaño': '1500 m2', 'precio': '$450,000'},
    {'numero': '3', 'tamaño': '3000 m2', 'precio': '$700,000'},
    {'numero': '4', 'tamaño': '2000 m2', 'precio': '$100,000'}
]

clientes = []

def disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila_idx, fila in enumerate(matrizLote, start=1):
        for col_idx, lote in enumerate(fila, start=1):
            if lote == ' ':
                print(f"[ ]", end="")
            else:
                print("[X]", end=" ")
        print()

def seleccionar_lote():
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su número de teléfono: ")
    email = input("Ingrese su dirección de correo electrónico: ")

    fila = int(input("Ingrese el número de fila del lote: "))
    columna = int(input("Ingrese el número de columna del lote: "))

    if fila < 1 or fila > len(matrizLote) or columna < 1 or columna > len(matrizLote[0]):
        print("Las coordenadas no son válidas, intente nuevamente.")
        return

    if matrizLote[fila - 1][columna - 1] == ' ':
        matrizLote[fila - 1][columna - 1] = 'X'
        clientes.append({'RUT': rut, 'Nombre': nombre, 'Teléfono': telefono, 'Email': email})
        print("Lote seleccionado!")
    else:
        print("El lote seleccionado no está disponible. Por favor, elija otro lote.")

def mostrar_detalles_lote():
    if len(clientes) == 0:
        print("No se han seleccionado lotes, por favor seleccione uno.")
        return

    cliente = clientes[-1]
    lote = lotes[len(clientes) - 1]

    print("Detalles del lote seleccionado:")
    print(f"Número de lote: {lote['numero']}")
    print(f"Tamaño del terreno: {lote['tamaño']}")
    print(f"Precio: {lote['precio']}")
    print(f"Cliente: {cliente['Nombre']}")
    print(f"RUT: {cliente['RUT']}")
    print(f"Teléfono: {cliente['Teléfono']}")
    print(f"Email: {cliente['Email']}")

def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['Nombre']}")
        print(f"RUT: {cliente['RUT']}")
        print(f"Teléfono: {cliente['Teléfono']}")
        print(f"Email: {cliente['Email']}")
        print()

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver clientes")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            disponibilidad_lotes()
        elif opcion == '2':
            seleccionar_lote()
        elif opcion == '3':
            mostrar_detalles_lote()
        elif opcion == '4':
            mostrar_clientes()
        elif opcion == '5':
            print("¡Muchas gracias! ¡Vuelva pronto!")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción correcta.")

main()
