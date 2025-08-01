from .personagem import Personagem
from simulador.relatorios import RelatorioUsarEspecial


class Mago(Personagem):
    def __init__(self, nome: str="CharacterMage", vida: int=90, ataque: int=8, mana: int=120) -> None:
        super().__init__(nome, vida, ataque, mana)

        self.mana = self.mana_maxima = mana

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

                relatorio_especial = {
                    **alvo.receber_dano(self.ataque * 5),
                    "nome_atacante": self.nome,
                    "mana_restante": self.mana,
                    "especial": True,
                    "especial_cooldown": self.especial_cooldown,
                    "motivo_erro_especial": None
                }
            
            else:
                self.especial_cooldown = max(0, self.especial_cooldown - 1)

        return relatorio_especial
