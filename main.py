import os
from readchar import readkey

def update_terminal(tecla, contador: int):
        match tecla:
            case "n":
                os.system("cls" if os.name == "nt" else "clear")
                print(contador)
                return 1
            case _:
                return 0

contador = 0
while(True):
    tecla = readkey()
    contador += update_terminal(tecla=tecla, contador=contador)
    if (contador > 50): break
