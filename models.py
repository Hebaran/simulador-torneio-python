from random import random

class Personagem:
    def __init__(self, nome="Character", vida=100, ataque=10):
        self.nome = nome.strip().capitalize()
        self.vida = self.vida_maxima = vida
        self.ataque = ataque


    def atacar(self, alvo):
        relatorio_ataque = {}
        
        if self.status_vida() and alvo.status_vida():
            relatorio_dano_causado = alvo.receber_dano(self.ataque)
            relatorio_ataque = relatorio_dano_causado | {"atacante": self.nome}

        return relatorio_ataque

    
    def receber_dano(self, dano=1):
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

class Guerreiro(Personagem):
    def __init__(self, nome="CharacterWarrior", vida=105, ataque=14):
        super().__init__(nome, vida, ataque)
    
    
    def atacar(self, alvo):
        relatorio_ataque = {}

        if self.status_vida() and alvo.status_vida():
            chance_critico = random() <= 0.2
            relatorio_dano_causado = alvo.receber_dano((self.ataque * 2) if chance_critico else self.ataque)
            relatorio_ataque = relatorio_dano_causado | {"atacante": self.nome, "critico": chance_critico}
            
        return relatorio_ataque


class Mago(Personagem):
    def __init__(self, nome="CharacterMage", vida=90, ataque=8, mana=120):
        super().__init__(nome, vida, ataque)
        self.mana = self.mana_maxima = mana


    def especial(self, alvo):
        relatorio_especial = {}

        if self.status_vida() and alvo.status_vida():
            relatorio_especial["especial"] = self.mana >= 60
            if relatorio_especial["especial"]:
                self.mana -= 60
        
        return relatorio_especial