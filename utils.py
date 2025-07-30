from os import system, name

def limpar_terminal():
    system("cls" if name == "nt" else "clear")


def subir_linha():
    return "\033[1A\r"


def narrador_combate(relatorio, atacante, defensor):
    duelistas = relatorio.get("duelistas")
    nome_duelista1 = duelistas[0].nome
    nome_duelista2 = duelistas[1].nome
    
    nome_atacante = atacante.nome
    nome_defensor = defensor.nome
    turno = relatorio.get("turno")
    dano_causado = relatorio.get("dano_causado")
    critico = relatorio.get("critico")
    especial = relatorio.get("especial")
    motivo_erro_especial = relatorio.get("motivo_erro_especial")
    especial_cooldown = relatorio.get("especial_cooldown")
    
    print(f"======= {nome_duelista1} x {nome_duelista2} =======")
    print(f"Turno: {turno}/100\n")
    
    for duelista in duelistas:
        if hasattr(duelista, "mana") and motivo_erro_especial:
            print(motivo_erro_especial)
            if motivo_erro_especial == "Especial em tempo de recarga":
                print(f"Faltam {especial_cooldown + 1} turno(os) para {nome_atacante} conseguir utilizar seu especial")
            break
    
    print(f"{nome_atacante} ataca {nome_defensor}.")
    
    if motivo_erro_especial or not hasattr(atacante, "mana"):
        print(f"{nome_atacante} utiliza um ataque básico.")

    if especial:
        print(f"{nome_atacante} UTILIZA SEU ESPECIAL!")
    elif critico:
        print("GOLPE CRÍTICO! ", end="")
        
    print(f"{nome_defensor} recebe {dano_causado} de dano.\n")
    
    for duelista in duelistas:
        print(f"Vida restante de {duelista.nome}: {duelista.vida}", f"| Mana restante de {duelista.nome}: {duelista.mana}" if hasattr(duelista, "mana") else "")
