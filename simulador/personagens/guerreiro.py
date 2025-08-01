from simulador.personagens.personagem import Personagem
from simulador.relatorios import RelatorioAtaque, RelatorioReceberDano
from dataclasses import dataclass
import random as _random


@dataclass
class Guerreiro(Personagem):
    vida: int = 105
    ataque: int = 13


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
            chance_critico: bool = _random.random() <= 0.2
            relatorio_dano_causado: RelatorioReceberDano = alvo.receber_dano((self.ataque * 2) if chance_critico else self.ataque)
            
            relatorio_ataque = {
            **relatorio_dano_causado,
            "nome_atacante": self.nome,
            "vida_restante_atacante": self.vida,
            "critico": chance_critico
        }

        return relatorio_ataque
