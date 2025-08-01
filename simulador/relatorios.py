from typing import TypedDict, Optional


class RelatorioReceberDano(TypedDict):
    nome_alvo: str
    dano_causado: int
    vida_restante_alvo: int


class RelatorioAtaque(RelatorioReceberDano):
    nome_atacante: str
    vida_restante_atacante: int


class RelatorioUsarEspecial(RelatorioReceberDano):
    nome_atacante: str
    especial: bool
    especial_cooldown: int
    mana_restante: int
    motivo_erro_especial: Optional[str]


class RelatorioRestaurarMana(TypedDict):
    mana_restaurada: int


class RelatorioRestaurarHp(TypedDict):
    vida_restaurada: int


class RelatorioRestaurarCd(TypedDict):
    cooldown_restaurado: bool
