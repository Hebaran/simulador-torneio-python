from simulador.personagens import Personagem
from typing import Dict, Any, Union

class Narrador:
    @staticmethod
    def narrar_combate(relatorio: Dict[str, Any], atacante: "Personagem", defensor: "Personagem") -> None:
        duelistas: list["Personagem"] = relatorio["duelistas"]
        nome_duelista1 = duelistas[0].nome
        nome_duelista2 = duelistas[1].nome
        nome_atacante = atacante.nome
        nome_defensor = defensor.nome
    
        turno: int = relatorio["turno"]
        dano_causado: int = relatorio["dano_causado"]
        critico: Union[bool, None] = relatorio.get("critico")
        especial: Union[bool, None] = relatorio.get("especial")
        motivo_erro_especial: Union[str, None] = relatorio.get("motivo_erro_especial") if atacante.possui_mana() else None
        especial_cooldown: Union[int, None] = relatorio.get("especial_cooldown")
    
        Narrador._narrar_turno(turno, nome_duelista1, nome_duelista2)
    
        for duelista in duelistas:
            if duelista.possui_mana() and motivo_erro_especial:
                print(motivo_erro_especial)
                if motivo_erro_especial == "Especial em tempo de recarga" and especial_cooldown is not None:
                    print(f"Faltam {especial_cooldown + 1} turno(os) para {nome_atacante} conseguir utilizar seu especial")
                break
    
        print(f"{nome_atacante} ataca {nome_defensor}.")
    
        if motivo_erro_especial or not atacante.possui_mana():
            print(f"{nome_atacante} utiliza um ataque básico.")
    
        if especial:
            print(f"{nome_atacante} UTILIZA SEU ESPECIAL!")
        elif critico:
            print("GOLPE CRÍTICO! ", end="")
    
        print(f"{nome_defensor} recebe {dano_causado} de dano.\n")
    
        for duelista in duelistas:
            print(f"Vida restante de {duelista.nome}: {duelista.vida} | Mana restante de {duelista.nome}: {duelista.mana}")


    @staticmethod
    def _narrar_turno(turno:int, nome_duelista1: str, nome_duelista2: str) -> None:
        print(f"======= {nome_duelista1} x {nome_duelista2} =======")
        print(f"Turno: {turno}/100\n")
