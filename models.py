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


    @classmethod
    def create_char(cls, nome: str, vida: tuple=(200, 240), ataque: tuple=(10, 15)) -> "Personagem":
        cls.vida = _random.randint(*vida)
        cls.ataque = _random.randint(*ataque)
        
        return cls(nome, cls.vida, cls.ataque)


class Guerreiro(Personagem):
    def __init__(self, nome: str="CharacterWarrior", vida: int=105, ataque: int=13) -> None:
        super().__init__(nome, vida, ataque)
    
    
    def atacar(self, alvo: "Personagem") -> Dict[str, Any]:
        relatorio_ataque: Dict[str, Any] = {}

        if self.status_vida() and alvo.status_vida():
            chance_critico: bool = _random.random() <= 0.2
            relatorio_dano_causado: Dict[str, Any] = alvo.receber_dano((self.ataque * 2) if chance_critico else self.ataque)
            relatorio_ataque = relatorio_dano_causado | {"atacante": self.nome, "critico": chance_critico}
            
        return relatorio_ataque


class Mago(Personagem):
    def __init__(self, nome: str="CharacterMage", vida: int=90, ataque: int=8, mana: int=120) -> None:
        super().__init__(nome, vida, ataque, mana)
        
        self.mana = self.mana_maxima = mana
        self.especial_cooldown = 0

    def usar_especial(self, alvo: "Personagem") -> Dict[str, Any]:
        relatorio_especial: Dict[str, Any] = {}

        if self.status_vida() and alvo.status_vida():   
            if self.mana >= 60 and self.especial_cooldown == 0:
                self.mana = max(0, self.mana - 60)
                self.especial_cooldown = 2
                
                relatorio_especial = {"atacante": self.nome, "especial": True, "mana_restante": self.mana}
                relatorio_especial.update(alvo.receber_dano(self.ataque * 5))
            else:
                self.especial_cooldown = max(0, self.especial_cooldown - 1)
                
                relatorio_especial= {
                    "especial": False,
                    "motivo_erro_especial": "Mana insuficiente" if self.mana <= 60 else "Especial em tempo de recarga",
                    "especial_cooldown": self.especial_cooldown
                }
        
        return relatorio_especial
