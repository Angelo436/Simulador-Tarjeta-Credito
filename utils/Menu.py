import msvcrt
import subprocess


def menu(opciones : dict) -> tuple:
    seleccion = 0

    while True:
        
        subprocess.call("cls",shell=True)

        print("Seleccione el tipo de operación:\n")

        for i, opcion in enumerate(opciones):
            if i == seleccion:
                print(f"❯ {opcion}")
            else:
                print(f"  {opcion}")

        tecla = msvcrt.getch()

        if tecla == b"\xe0":
            # Teclas especiales: flechas
            tecla = msvcrt.getch()

            if tecla == b"H":      # Flecha arriba
                seleccion = (seleccion - 1) % len(opciones)

            elif tecla == b"P":    # Flecha abajo
                seleccion = (seleccion + 1) % len(opciones)

        elif tecla == b"\r":
            # Enter
            key = list(opciones.keys())[seleccion]
            value = opciones[key]
            subprocess.call("cls",shell=True)

            if key == "Compra":
                value = int(input("Cantidad de cuotas: "))

            return key, value
