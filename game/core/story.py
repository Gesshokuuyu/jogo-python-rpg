# game/story.py

from game.entities.enemy import Enemy
from game.core.combat import iniciar_combate

def inicio(player):
    print("\nVocê chega à vila de Lyris...")

    escolha = input("1 - Ir para floresta | 2 - Taverna\n> ")

    if escolha == "1":
        floresta(player)
    else:
        taverna(player)

def floresta(player):
    print("\nVocê entra na floresta...")
    print("\n Você sente uma presença sombria, olha para o lado e...")
    inimigo = Enemy("Criatura Sombria", 30, 5, 2)

    comabt = iniciar_combate(player, inimigo)

    if(comabt):
        print(f"\n A Batalha foi dificil, mas você venceu, deseja lootear a {inimigo.nome}?")
        print("\n 1 - Sim | 2 - Não\n> ")

def taverna(player):
    print("\nUm velho fala sobre a Torre de Morvak...")