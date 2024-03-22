

import random
import lista_heroi1

import lista_oponentes

Enredo = (input("Em um reino muito distante,acontece o torneio dos jogos anuais de Dragoes e herois ,onde herois enfrentam dragoes por puro esporte,e os mesmos competem pela vitoria e pelotitulo de heroi ou dragao mais forte"))


Start = input("escolha seu personagem:")
print(Start + "1- thor/2-zeus")




escolha = int(input("digite o numero do heroi"))
if escolha == 1:
    fala = ["eu sou o thor e irei derrotar todos em meu caminho!"]
    for fala in fala:
        if fala == print(fala):
            break

else:
    fala = ["sou o mais poderoso dos dragoes ,ninguem se compara a mim !"]
    for fala in fala:
        if fala == print(fala):
            break
heroi_escolhido = lista_heroi1.lista_heroi[escolha-1]
oponente = lista_oponentes.lista_oponente[random.randrange(1,2)]

while heroi_escolhido.vida > 0 and oponente.vida > 0:
    heroi_escolhido.atacar(oponente)
    oponente.atacar(heroi_escolhido)
if heroi_escolhido.vida > 0:
    print(f"{heroi_escolhido.nome} venceu {oponente.nome}")
else:
    print(f"{heroi_escolhido.nome} foi derrotado por {oponente.nome}")








