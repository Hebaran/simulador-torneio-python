from models import Personagem
from utils import limpar_terminal
from random import shuffle, sample
from time import sleep

nomes_possiveis = ["Mago", "Bárbaro", "Guerreiro", "Arqueiro", "Ladino", "Assassino"]
vidas_possiveis = [100, 80, 90, 110, 120, 105]
ataques_possiveis = [10, 15, 8, 12, 9, 14]
lutadores = []

for i in range(1, 7):
    shuffle(nomes_possiveis)
    shuffle(vidas_possiveis)
    shuffle(ataques_possiveis)

    nome_char = nomes_possiveis.pop()
    vida_char = vidas_possiveis.pop()
    ataque_char = ataques_possiveis.pop()

    lutadores.append(Personagem(nome_char, vida_char, ataque_char))

while len(lutadores) > 1:
    duelistas = sample(lutadores, 2)
    atacante, defensor = duelistas

    for turno in range(1, 101):
        if False in {atacante.status_vida(), defensor.status_vida()}:
            ganhador = atacante if atacante.status_vida() else defensor
            perdedor = defensor if atacante.status_vida() else atacante
            
            ganhador.restaurar_hp()
            lutadores.remove(perdedor)
            break
            
        if turno % 2 == 1:
            atacante = duelistas[0]
            defensor = duelistas[1]
        else:
            atacante = duelistas[1]
            defensor = duelistas[0]

        limpar_terminal()
        print(f"======= {duelistas[0].nome} x {duelistas[1].nome} =======")
        print(f"Turno: {turno}/100\n")

        relatorio_escolhido = atacante.atacar(defensor)
        sleep(0.25)

    sleep(1)

limpar_terminal()
print(f"Parabéns, {lutadores[0].nome} é o ganhador do torneio!")
