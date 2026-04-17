# game/locations/tower.py

import random
from game.entities.enemy import Enemy
from game.core.combat import iniciar_combate
from game.core.ui import (
    titulo, narrar, menu, escolha, aviso, sucesso,
    subtitulo, separador, tela_vitoria,
    COR_MENU, COR_BOSS, COR_DANO, limparUI
)
from colorama import Style

INIMIGOS_TORRE = ["e-cavaleiro", "e-espectro"]


def torre(player):
    """Torre de Morvak — local final com boss"""
    titulo("TORRE DE MORVAK")
    narrar("Uma torre negra se ergue contra o céu vermelho.")
    narrar("Relâmpagos cortam as nuvens ao redor do topo da torre...")
    narrar("Você empurra os portões de ferro e entra.")

    # --- Andar 1 ---
    subtitulo("1º ANDAR — Salão dos Cavaleiros")
    narrar("Armaduras se alinham nas paredes... mas uma delas se move!")

    enemy1 = Enemy("e-cavaleiro")
    res1 = iniciar_combate(player, enemy1)
    if not res1:
        if res1 is False:
            return
        narrar("Você foge da torre por enquanto...")
        return

    # --- Andar 2 ---
    subtitulo("2º ANDAR — Câmara dos Espectros")
    narrar("O ar gela conforme você sobe as escadas.")
    narrar("Vultos transparentes flutuam pela câmara...")

    enemy2 = Enemy("e-espectro")
    res2 = iniciar_combate(player, enemy2)
    if not res2:
        if res2 is False:
            return
        narrar("Você recua da torre...")
        return

    # --- Descanso antes do boss ---
    separador()
    narrar("Você encontra uma sala tranquila com uma fonte de água cristalina.")
    menu(["Descansar na fonte (recuperar HP/Mana)", "Seguir em frente"])
    op = escolha(validas=["1", "2"])

    limparUI()

    if op == "1":
        player.descansar()
        sucesso(f"HP e Mana restaurados! ({player.hp}/{player.hp_max} HP)")

    # --- BOSS FINAL ---
    subtitulo("TOPO DA TORRE — Salão do Trono")
    print(COR_BOSS + Style.BRIGHT + """
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║    ☠  MORVAK, O SENHOR DAS SOMBRAS  ☠   ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """)
    narrar("Uma figura sombria se levanta do trono de ossos.", velocidade=0.04)
    narrar('"Então... você chegou até aqui. Impressionante."', velocidade=0.04)
    narrar('"Mas sua jornada termina AGORA!"', velocidade=0.03)

    morvak = Enemy("e-morvak")
    resultado = iniciar_combate(player, morvak)

    if resultado is True:
        player.capitulo = 4
        tela_vitoria()
        narrar("A torre começa a desmoronar ao seu redor.", velocidade=0.04)
        narrar("Você escapa pelos portões enquanto pedras caem.", velocidade=0.03)
        narrar("Do lado de fora, o sol nasce sobre Lyris pela primeira vez em anos.", velocidade=0.04)
        narrar("Seu nome será cantado em todas as tavernas do reino.", velocidade=0.03)

        print(COR_MENU + "\n  Obrigado por jogar Lendas de Lyris!")
        print(COR_MENU + "  Desenvolvido em Python com ♥\n")
        return True
    else:
        return False
