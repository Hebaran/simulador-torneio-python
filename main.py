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
    atacante, defensor = sample(lutadores, 2)
    atacante_vida_backup = atacante.vida
    defensor_vida_backup = defensor.vida
    
    for turno in range(1, 101):
        if False in {atacante.status_vida(), defensor.status_vida()}:
            break
        
        limpar_terminal()
        print(f"======= {atacante.nome} x {defensor.nome} =======")
        print(f"Turno: {turno}/100\n")
        
        if turno % 2 == 1:
            escolhido = atacante
            proximo = defensor
        else:
            escolhido = defensor
            proximo = atacante
        
        relatorio_escolhido = escolhido.atacar(proximo)
        sleep(0.25)
            
    if atacante.status_vida():
        atacante.vida = atacante_vida_backup
        perdedor = defensor
    else:
        defensor.vida = defensor_vida_backup
        perdedor = atacante

    lutadores.remove(perdedor)
    sleep(1)

limpar_terminal()
print(f"Parabéns, {lutadores[0].nome} é o ganhador do torneio!")
