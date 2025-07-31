from os import system, name


def limpar_terminal() -> None:
    system("cls" if name == "nt" else "clear")
