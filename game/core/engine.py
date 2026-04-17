# game/core/engine.py

from colorama import init
from game.entities.player import Player
from game.core.classe import escolher_classe
from game.core.story import inicio
from game.core.ui import tela_titulo, narrar, separador, escolha, limparUI, COR_MENU
from game.core.sound import tocar_musica


def iniciar_jogo():
    init(autoreset=True)

    tela_titulo()

    print(COR_MENU + "  Pressione ENTER para começar...")
    input()

    separador()
    nome = input(COR_MENU + "  Digite o nome do seu personagem: ").strip()
    if not nome:
        nome = "Herói"

    player = Player(nome)
    limparUI()

    escolher_classe(player)
    limparUI()


    narrar(f"\nBem-vindo, {player.nome} o {player.classe}! Sua aventura começa agora...")

    inicio(player)