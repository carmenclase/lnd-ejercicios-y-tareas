import json

nombre_fichero = input("Escriba el nombre del fichero .json: ")

def leer_fichero(fichero):
    with open(fichero, "r") as archivo:
        datos = json.load(archivo)

        if isinstance(datos, list):
            print("Contenido del archivo JSON:")
            for i, item in enumerate(datos, start=1):
                print(f"\nRegistro {i}:")
                for clave, valor in item.items():
                    print(f"{clave}: {valor}")
        else:
            print("El contenido del fichero .json no es una lista")

leer_fichero(nombre_fichero)