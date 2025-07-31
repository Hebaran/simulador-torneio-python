from .personagem import Personagem
from typing import Dict, Any


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
