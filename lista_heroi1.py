
class personagem:
    def __init__(self, nome, vida, ataque):
       self.nome = nome
       self.vida = vida
       self.ataque = ataque

    def salvar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f"{self.nome},{self.vida},{self.ataque}\n")

    @classmethod
    def recuperar_arquivo(cls, nome_arquivo):
        personagens = []
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, hp, atk = linha.strip().split(',')
                personagem = cls(nome, int(hp), int(atk), [])
                personagens.append(personagem)
        return personagens
        
class jogador (personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        self.nivel = 1
    def atacar(self,alvo):
        dano = self.ataque
        alvo.vida = alvo.vida - dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")




lista_heroi = [jogador("zeus", 1150, 500), jogador("thor", 1500, 600)]

