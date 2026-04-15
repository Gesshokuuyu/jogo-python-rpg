# game/engine.py

from game.entities.player import Player
from game.core.story import inicio

def iniciar_jogo():
    nome = input("Digite o nome do seu personagem: ")
    player = Player(nome)

    inicio(player)