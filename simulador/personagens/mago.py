from simulador.personagens.personagem import Personagem
from simulador.relatorios import RelatorioUsarEspecial, RelatorioReceberDano
from dataclasses import dataclass


@dataclass
class Mago(Personagem):
    vida: int = 90
    ataque: int = 8
    mana: int = 120


    def usar_especial(self, alvo: "Personagem") -> RelatorioUsarEspecial:
        relatorio_especial: RelatorioUsarEspecial = {
            "nome_alvo": alvo.nome,
            "dano_causado": 0,
            "vida_restante_alvo": alvo.vida,
            "nome_atacante": self.nome,
            "mana_restante": self.mana,
            "especial": False,
            "especial_cooldown": self.especial_cooldown,
            "motivo_erro_especial": "Mana insuficiente" if self.mana <= 60 else "Especial em tempo de recarga"
        }

        if self.status_vida() and alvo.status_vida():   
            if self.mana >= 60 and self.especial_cooldown == 0:
                self.mana = max(0, self.mana - 60)
                self.especial_cooldown = 2
                
                relatorio_dano_causado: RelatorioReceberDano = alvo.receber_dano(self.ataque * 5)

                relatorio_especial = {
                    **relatorio_dano_causado,
                    "nome_atacante": self.nome,
                    "mana_restante": self.mana,
                    "especial": True,
                    "especial_cooldown": self.especial_cooldown,
                    "motivo_erro_especial": None
                }
            
            else:
                self.especial_cooldown = max(0, self.especial_cooldown - 1)

        return relatorio_especial
