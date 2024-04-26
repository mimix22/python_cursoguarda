
import sqlite3



conn = sqlite3.connect("heroes_dragoes.db")
cursor = conn.cursor()

#criação da tabela para herois

cursor.execute('''CREATE TABLE IF NOT EXISTS heroes 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                health INTEGER,
                attack INTEGER)''')

#criação da tabela para dragoes
cursor.execute('''CREATE TABLE IF NOT EXISTS dragons 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 health INTEGER,
                 attack INTEGER)''')

conn.commit()
conn.close()
class personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def salvar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f"{self.nome},{self.vida},{self.ataque}\n")
    def insert_dragon(dragon):
        conn = sqlite3.connect("heroes_dragoes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dragons (name, health,  attack) VALUES (?, ?, ?)",
                       (dragon.nome, dragon.vida, dragon.ataque))
        conn.commit()
        conn.close()

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

    def get_dragons():
        conn = sqlite3.connect("heroes_dragoes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dragons")
        dragons_data = cursor.fetchall()
        conn.close()

        dragons = [oponente(*data[1:]) for data in dragons_data]
        return dragons
class oponente (personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)
        self.nivel = 1
    def atacar(self,alvo):
        dano = self .ataque
        alvo.vida = alvo.vida - dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano}de dano.")





lista_oponente = [oponente ("fireDragon", 3200, 950), oponente("iceDragon", 2120, 840)]


