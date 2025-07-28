class Personagem:
    def __init__(self, nome="Character", vida=100, ataque=10):
        self.nome = nome.strip().capitalize()
        self.vida = self.vida_maxima = vida
        self.ataque = ataque


    def atacar(self, alvo):
        relatorio_ataque = {}
        
        if self.status_vida() and alvo.status_vida():
            alvo.vida = max(0, alvo.vida - self.ataque)

            relatorio_ataque["atacante"] = self.nome
            relatorio_ataque["alvo"] = alvo.nome
            relatorio_ataque["dano_causado"] = self.ataque
            relatorio_ataque["vida_restante_alvo"] = alvo.vida

        return relatorio_ataque

    
    def receber_dano(self, dano=1):
        relatorio_dano = {}
        
        if self.status_vida():
            self.vida = max(0, self.vida - dano)

            relatorio_dano["alvo"] = self.nome
            relatorio_dano["dano_causado"] = dano
            relatorio_dano["vida_restante_alvo"] = self.vida
            # Misteriosamente PERSONAGEM recebeu QTD_DANO de dano.
            # Vida restante de PERSONAGEM: VIDA_RESTANTE}

        return relatorio_dano


    def restaurar_hp(self):
        relatorio_hp = {}

        self.vida = self.vida_maxima
        relatorio_hp["vida_restaurada"] = self.vida_maxima
        
        return relatorio_hp

    
    def status_vida(self):
        return self.vida > 0
