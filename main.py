from models import Personagem, Guerreiro, Mago
from utils import limpar_terminal, narrador_combate
from random import sample
from time import sleep

nomes_lutadores = ["Bárbaro", "Arqueiro", "Ladino", "Assassino"]
lutadores = []

for nome in nomes_lutadores:
    lutadores.append(Personagem.create_char(nome))
lutadores.extend([Guerreiro("Guerreiro", 235), Mago("Mago", 190)])

while len(lutadores) > 1:
    duelistas = sample(lutadores, 2)
    atacante, defensor = duelistas

    for turno in range(1, 101):
        if False in {atacante.status_vida(), defensor.status_vida()}:
            ganhador = atacante if atacante.status_vida() else defensor
            perdedor = defensor if atacante.status_vida() else atacante
            
            if hasattr(ganhador, "mana"):
                ganhador.restaurar_mana()
            
            ganhador.restaurar_hp()
            lutadores.remove(perdedor)
            break
            
        if turno % 2 == 1:
            atacante = duelistas[0]
            defensor = duelistas[1]
        else:
            atacante = duelistas[1]
            defensor = duelistas[0]

        relatorio_atacante = {}
        try:
            atacante.mana = min(atacante.mana + 15, atacante.mana_maxima)
            relatorio_atacante = atacante.usar_especial(defensor)
            
            if not relatorio_atacante["especial"]:
                raise PermissionError(relatorio_atacante["motivo_erro_especial"])
        except (AttributeError, PermissionError):
            if hasattr(atacante, "mana"):
                relatorio_atacante.update(atacante.atacar(defensor))
            else:
                relatorio_atacante = atacante.atacar(defensor)

        limpar_terminal()
        narrador_combate(relatorio_atacante | {"turno": turno, "duelistas": duelistas}, atacante, defensor)
        sleep(0.5)
    sleep(1)

limpar_terminal()
print(f"Parabéns, {lutadores[0].nome} é o ganhador do torneio!")
