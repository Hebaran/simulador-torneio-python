from .personagem import Personagem
import random as _random
from typing import Dict, Any


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
