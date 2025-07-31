from models import Personagem, Guerreiro, Mago
from utils import narrador_combate, limpar_terminal
from typing import Dict, Any
from random import sample

nomes_lutadores: list[str] = ["Bárbaro", "Arqueiro", "Ladino", "Assassino"]

lutadores: list["Personagem"] = [Personagem.create_char(nome) for nome in nomes_lutadores] 
lutadores.extend([Guerreiro("Guerreiro", 235), Mago("Mago", 190)])

while len(lutadores) > 1:
    duelistas = sample(lutadores, 2)
    atacante, defensor = duelistas

    for turno in range(1, 101):
        if False in [atacante.status_vida(), defensor.status_vida()]:
            ganhador = atacante if atacante.status_vida() else defensor
            perdedor = defensor if atacante.status_vida() else atacante

            ganhador.restaurar_hp()
            ganhador.restaurar_mana()
            
            lutadores.remove(perdedor)
            break
            
        if turno % 2 == 1:
            atacante = duelistas[0]
            defensor = duelistas[1]
        else:
            atacante = duelistas[1]
            defensor = duelistas[0]

        relatorio_atacante: Dict[str, Any] = {}
        
        atacante.mana = min(atacante.mana + 15, atacante.mana_maxima)
        relatorio_atacante = atacante.usar_especial(defensor)
        
        if not relatorio_atacante["especial"]:
            relatorio_atacante.update(atacante.atacar(defensor))

        limpar_terminal()
        narrador_combate(relatorio_atacante | {"turno": turno, "duelistas": duelistas}, atacante, defensor)
        input("\nPressione ENTER para ir para o próximo Turno")

limpar_terminal()
print(f"Parabéns, {lutadores[0].nome} é o ganhador do torneio!")
