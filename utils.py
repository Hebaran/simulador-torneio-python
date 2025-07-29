from os import system, name

def limpar_terminal():
    system("cls" if name == "nt" else "clear")


def subir_linha():
    return "\033[1A\r"
