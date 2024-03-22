
class personagem:
    def __init__(self, nome, vida, ataque):
       self.nome = nome
       self.vida = vida
       self.ataque = ataque
class jogador (personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        self.nivel = 1
    def atacar(self,alvo):
        dano = self.ataque
        alvo.vida = alvo.vida - dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")


lista_heroi = [jogador("zeus", 1150, 500), jogador("thor", 1500, 600)]

