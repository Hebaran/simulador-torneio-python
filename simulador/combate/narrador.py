from simulador.personagens import Personagem
from typing import Dict, Any, Union

class Narrador:
    
    @staticmethod
    def _narrar_combate(relatorio: Dict[str, Any], atacante: "Personagem", defensor: "Personagem") -> str:
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
    
        relatorio_narrador = Narrador._narrar_turno(turno, nome_duelista1, nome_duelista2)
        if critico:
            relatorio_narrador += Narrador._narrar_critico()
        if especial:
            relatorio_narrador += Narrador._narrar_especial(nome_atacante)
        else:
            if atacante.possui_mana() and motivo_erro_especial:
                relatorio_narrador += Narrador._narrar_erro_especial(nome_atacante, motivo_erro_especial, especial_cooldown)
        relatorio_narrador += Narrador._narrar_ataque(nome_atacante, nome_defensor, dano_causado, especial)
        relatorio_narrador += Narrador._narrar_vida_mana_restante(duelistas)
        
        return relatorio_narrador


    @staticmethod
    def _narrar_turno(turno: int, nome_duelista1: str, nome_duelista2: str) -> str:
        relatorio_narrador = (
            f"======= {nome_duelista1} x {nome_duelista2} =======\n"
            f"Turno: {turno}/100\n\n"
        )
        return relatorio_narrador
    
    
    @staticmethod
    def _narrar_especial(nome_atacante: str) -> str:
        relatorio_narrador = f"{nome_atacante} UTILIZA SEU ESPECIAL!\n"
        return relatorio_narrador

    
    @staticmethod
    def _narrar_critico() -> str:
        relatorio_narrador = "GOLPE CRÍTICO! "
        return relatorio_narrador
    
    
    @staticmethod
    def _narrar_ataque(nome_atacante: str, nome_defensor: str, dano_causado: int, especial: Union[bool, None]) -> str:
        relatorio_narrador = ""
        if not especial:
            relatorio_narrador = f"{nome_atacante} utiliza um ataque básico.\n"
        relatorio_narrador += f"{nome_atacante} ataca {nome_defensor}.\n"
        relatorio_narrador += f"{nome_defensor} recebe {dano_causado} de dano.\n"
        return relatorio_narrador
    
    
    @staticmethod
    def _narrar_erro_especial(nome_atacante: str, motivo_erro_especial: Union[str, None], especial_cooldown: Union[int, None]) -> str:
        relatorio_narrador: str = f"{motivo_erro_especial}\n"
        
        if motivo_erro_especial == "Especial em tempo de recarga" and especial_cooldown is not None:
            relatorio_narrador += f"Faltam {especial_cooldown + 1} turno(os) para {nome_atacante} conseguir utilizar seu especial\n"
        return relatorio_narrador
    
    
    @staticmethod
    def _narrar_vida_mana_restante(duelistas: list["Personagem"]) -> str:
        relatorio_narrador = "\n"
        for duelista in duelistas:
            relatorio_narrador += f"Vida restante de {duelista.nome}: {duelista.vida} | Mana restante de {duelista.nome}: {duelista.mana}\n"
        return relatorio_narrador
