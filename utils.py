from os import system, name

def limpar_terminal():
    system("cls" if name == "nt" else "clear")

