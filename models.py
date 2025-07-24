class Personagem:
    def __init__(self, nome="Character", vida=100, ataque=10):
        self.nome = nome.capitalize()
        self.vida = vida
        self.ataque = ataque
        self.vivo = True


    def atacar(self, alvo):
        if self.vivo:
            dano = int(self.ataque *
                       1.5 if self.nome == "Herói" else self.ataque)

            if alvo.vivo:
                alvo.vida = max(0, alvo.vida - dano)

                print(f"{self.nome} ataca {alvo.nome}.")
                print(f"{alvo.nome} recebe {dano} de dano.")
                print(f"Vida restante de {alvo.nome}: {alvo.vida}")

                if alvo.vida == 0:
                    alvo.vivo = False
                    print(f"{self.nome} matou {alvo.nome}.")
            else:
                print(f"{alvo.nome} já está morto.")
        else:
            print(f"{self.nome} está morto e não consegue atacar.")

    
    def receber_dano(self, dano=1):
        if self.vivo:
            self.vida = max(0, self.vida - dano)
            print(f"Misteriosamente {self.nome} recebeu {dano} de dano.")
            print(f"Vida restante de {self.nome}: {self.vida}")

            if self.vida == 0:
                self.vivo = False
                print(f"{self.nome} morreu.")
        else:
            print(f"{self.nome} já está morto.")

    
    def status_vida(self):
        return self.vivo
