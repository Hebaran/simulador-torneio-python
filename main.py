from models import Personagem, Guerreiro, Mago
from utils import limpar_terminal
from random import shuffle, sample
from time import sleep

nomes_possiveis = ["Bárbaro", "Arqueiro", "Ladino", "Assassino"]
vidas_possiveis = [100, 80, 110, 120]
ataques_possiveis = [10, 15, 12, 9]
lutadores = []

for i in range(1, 5):
    shuffle(nomes_possiveis)
    shuffle(vidas_possiveis)
    shuffle(ataques_possiveis)

    nome_char = nomes_possiveis.pop()
    vida_char = vidas_possiveis.pop()
    ataque_char = ataques_possiveis.pop()

    lutadores.append(Personagem(nome_char, vida_char, ataque_char))
lutadores.append(Guerreiro("Guerreiro"))
lutadores.append(Mago("Mago"))

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

        if atacante.mana >= 0:
            atacante.mana = atacante.mana + 10 if atacante.mana <= atacante.mana_maxima - 10 else atacante.mana_maxima
        relatorio_atacante = atacante.atacar(defensor)
        
        limpar_terminal()
        print(f"======= {duelistas[0].nome} x {duelistas[1].nome} =======")
        print(f"Turno: {turno}/100\n")
        print(f"{relatorio_atacante["atacante"]} ataca {relatorio_atacante["alvo"]}.")
        if relatorio_atacante.get("critico"):
            print("CRÍTICO! ", end="")  
        print(f"{relatorio_atacante["alvo"]} recebe {relatorio_atacante["dano_causado"]} de dano.")
        print(f"Vida restante de {relatorio_atacante["alvo"]}: {relatorio_atacante["vida_restante_alvo"]}")
        
        sleep(0.25)

    sleep(1)

limpar_terminal()
print(f"Parabéns, {lutadores[0].nome} é o ganhador do torneio!")
