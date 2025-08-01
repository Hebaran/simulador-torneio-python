import random as _random
from dataclasses import dataclass
from simulador.relatorios import (
    RelatorioAtaque,
    RelatorioReceberDano,
    RelatorioUsarEspecial,
    RelatorioRestaurarMana,
    RelatorioRestaurarHp,
    RelatorioRestaurarCd
)


@dataclass
class Personagem:
    nome: str = "Character"
    vida: int = 100
    ataque: int = 10
    mana: int = 0
    especial_cooldown: int = 0
    
    
    def __post_init__(self) -> None:
        self.nome = self.nome.strip().capitalize()
        self.vida_maxima = self.vida
        self.mana_maxima = self.mana
    
    
    def atacar(self, alvo: "Personagem") -> RelatorioAtaque:
        relatorio_ataque: RelatorioAtaque = {
            "nome_alvo": alvo.nome,
            "dano_causado": 0,
            "vida_restante_alvo": alvo.vida,
            "nome_atacante": self.nome,
            "vida_restante_atacante": self.vida,
            "critico": False
        }
        
        if self.status_vida() and alvo.status_vida():
            relatorio_ataque = {
                **alvo.receber_dano(self.ataque),
                "nome_atacante": self.nome,
                "vida_restante_atacante": self.vida,
                "critico": False
            }
        
        return relatorio_ataque
    
    
    def receber_dano(self, dano: int = 1) -> RelatorioReceberDano:
        relatorio_receber_dano: RelatorioReceberDano = {
            "nome_alvo": self.nome,
            "dano_causado": 0,
            "vida_restante_alvo": self.vida
        }
        
        if self.status_vida():
            self.vida = max(0, self.vida - dano)
            relatorio_receber_dano["dano_causado"] = dano
            relatorio_receber_dano["vida_restante_alvo"] = self.vida
        
        return relatorio_receber_dano


    def usar_especial(self, alvo: "Personagem") -> RelatorioUsarEspecial:
        relatorio_especial: RelatorioUsarEspecial = {
            "nome_alvo": alvo.nome,
            "dano_causado": 0,
            "vida_restante_alvo": alvo.vida,
            "nome_atacante": self.nome,
            "especial": False,
            "especial_cooldown": self.especial_cooldown,
            "mana_restante": self.mana,
            "motivo_erro_especial": f"{self.nome} não tem um especial. Nada acontece com {alvo.nome}"
        }
        
        return relatorio_especial


    def restaurar_mana(self) -> RelatorioRestaurarMana:
        self.mana = self.mana_maxima
        relatorio_mana: RelatorioRestaurarMana = {"mana_restaurada": self.mana_maxima}
        
        return relatorio_mana
    
    
    def restaurar_hp(self) -> RelatorioRestaurarHp:
        self.vida = self.vida_maxima
        relatorio_hp: RelatorioRestaurarHp = {"vida_restaurada": self.vida_maxima}
        
        return relatorio_hp
    
    
    def restaurar_cd(self) -> RelatorioRestaurarCd:
        self.especial_cooldown = 0
        relatorio_cd: RelatorioRestaurarCd = {"cooldown_restaurado": True}
        
        return relatorio_cd
    
    
    def status_vida(self) -> bool:
        return self.vida > 0
    
    
    def possui_mana(self) -> bool:
        return self.mana_maxima > 0
    
    
    @classmethod
    def create_char(cls, nome: str, vida_range: tuple[int, int] = (200, 240), ataque_range: tuple[int, int] = (10, 15)) -> "Personagem":
        vida = _random.randint(*vida_range)
        ataque = _random.randint(*ataque_range)
        
        return cls(nome, vida, ataque)
