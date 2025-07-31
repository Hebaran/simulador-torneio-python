import random as _random

class Personagem:
    def __init__(self, nome: str="Character", vida: int=100, ataque: int=10) -> None:
        self.nome = nome.strip().capitalize()
        self.vida = self.vida_maxima = vida
        self.ataque = ataque


    def atacar(self, alvo: "Personagem") -> dict:
        relatorio_ataque: dict = {}
        
        if self.status_vida() and alvo.status_vida():
            relatorio_dano_causado = alvo.receber_dano(self.ataque)
            relatorio_ataque = relatorio_dano_causado | {"atacante": self.nome, "vida_restante_atacante": self.vida}

        return relatorio_ataque

    
    def receber_dano(self, dano: int=1):
        relatorio_dano = {}
        
        if self.status_vida():
            self.vida = max(0, self.vida - dano)

            relatorio_dano["alvo"] = self.nome
            relatorio_dano["dano_causado"] = dano
            relatorio_dano["vida_restante_alvo"] = self.vida

        return relatorio_dano


    def restaurar_hp(self):
        relatorio_hp = {}

        self.vida = self.vida_maxima
        relatorio_hp["vida_restaurada"] = self.vida_maxima
        
        return relatorio_hp

    
    def status_vida(self):
        return self.vida > 0


    @classmethod
    def create_char(cls, nome: str, vida: tuple=(200, 240), ataque: tuple=(10, 15)) -> object:
        cls.vida = _random.randint(*vida)
        cls.ataque = _random.randint(*ataque)
        
        return cls(nome, cls.vida, cls.ataque)


class Guerreiro(Personagem):
    def __init__(self, nome="CharacterWarrior", vida=105, ataque=14):
        super().__init__(nome, vida, ataque)
    
    
    def atacar(self, alvo):
        relatorio_ataque = {}

        if self.status_vida() and alvo.status_vida():
            chance_critico = _random.random() <= 0.2
            relatorio_dano_causado = alvo.receber_dano((self.ataque * 2) if chance_critico else self.ataque)
            relatorio_ataque = relatorio_dano_causado | {"atacante": self.nome, "critico": chance_critico}
            
        return relatorio_ataque


class Mago(Personagem):
    def __init__(self, nome="CharacterMage", vida=90, ataque=8, mana=120):
        super().__init__(nome, vida, ataque)
        self.mana = self.mana_maxima = mana
        self.especial_cooldown = 0

    def usar_especial(self, alvo):
        relatorio_especial = {}

        if self.status_vida() and alvo.status_vida():   
            if self.mana >= 60 and self.especial_cooldown == 0:
                self.mana = max(0, self.mana - 60)
                self.especial_cooldown = 2
                relatorio_especial.update(alvo.receber_dano(self.ataque * 5) | {"atacante": self.nome, "especial": True, "mana_restante": self.mana})
            else:
                self.especial_cooldown = max(0, self.especial_cooldown - 1)
                relatorio_especial= {"especial": False, "motivo_erro_especial": "Mana insuficiente" if self.mana <= 60 else "Especial em tempo de recarga", "especial_cooldown": self.especial_cooldown}
        
        return relatorio_especial
    
    
    def restaurar_mana(self):
        relatorio_mana = {}

        self.mana = self.mana_maxima
        relatorio_mana["mana_restaurada"] = self.mana_maxima
        
        return relatorio_mana
