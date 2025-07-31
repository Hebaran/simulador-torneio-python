import random as _random
from typing import Dict, Any

class Personagem:
    def __init__(self, nome: str="Character", vida: int=100, ataque: int=10, mana: int=0) -> None:
        self.nome = nome.strip().capitalize()
        self.vida = self.vida_maxima = vida
        self.ataque = ataque
        self.mana = self.mana_maxima = mana


    def atacar(self, alvo: "Personagem") -> Dict[str, Any]:
        relatorio_ataque: Dict[str, Any] = {}
        
        if self.status_vida() and alvo.status_vida():
            relatorio_ataque = alvo.receber_dano(self.ataque) | {"atacante": self.nome, "vida_restante_atacante": self.vida}

        return relatorio_ataque

    
    def receber_dano(self, dano: int=1) -> Dict[str, Any]:
        relatorio_dano: Dict[str, Any] = {}
        
        if self.status_vida():
            self.vida = max(0, self.vida - dano)
            relatorio_dano = {"alvo": self.nome, "dano_causado": dano, "vida_restante_alvo": self.vida}
            
        return relatorio_dano


    def usar_especial(self, alvo) -> Dict[str, Any]:
        relatorio_especial: Dict[str, Any] = {
            "especial": False,
            "motivo_erro_especial": f"{self.nome} não tem um especial. Nada acontece com {alvo.nome}"
        }

        return relatorio_especial


    def restaurar_mana(self) -> Dict[str, int]:
        self.mana = self.mana_maxima
        relatorio_mana: Dict[str, int] = {"mana_restaurada": self.mana_maxima}

        return relatorio_mana


    def restaurar_hp(self) -> Dict[str, int]:
        self.vida = self.vida_maxima
        relatorio_hp: Dict[str, int] = {"vida_restaurada": self.vida_maxima}

        return relatorio_hp

    
    def status_vida(self) -> bool:
        return self.vida > 0


    def possui_mana(self) -> bool:
        return self.mana_maxima > 0


    @classmethod
    def create_char(cls, nome: str, vida_range: tuple=(200, 240), ataque_range: tuple=(10, 15)) -> "Personagem":
        vida = _random.randint(*vida_range)
        ataque = _random.randint(*ataque_range)
        
        return cls(nome, vida, ataque)
