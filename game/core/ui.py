import sys
import time
from colorama import Fore, Style, init
import subprocess
import os

init(autoreset=True)


# =========================
# CORES TEMÁTICAS
# =========================

COR_TITULO = Fore.LIGHTYELLOW_EX
COR_DIALOGO = Fore.LIGHTCYAN_EX
COR_NPC = Fore.LIGHTGREEN_EX
COR_AVISO = Fore.YELLOW
COR_ERRO = Fore.LIGHTRED_EX
COR_DANO = Fore.RED
COR_CURA = Fore.GREEN
COR_OURO = Fore.YELLOW
COR_XP = Fore.LIGHTMAGENTA_EX
COR_ITEM = Fore.LIGHTCYAN_EX
COR_BOSS = Fore.LIGHTRED_EX
COR_MENU = Fore.LIGHTWHITE_EX
COR_MANA = Fore.LIGHTBLUE_EX
COR_NORMAL = Style.RESET_ALL


# =========================
# FUNÇÕES DE UI
# =========================


def limparUI():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)

def separador(char="═", tamanho=50):
    print(Fore.LIGHTBLACK_EX + char * tamanho)


def titulo(texto):
    separador("═")
    print(COR_TITULO + Style.BRIGHT + f"  ⚔  {texto}  ⚔  ")
    separador("═")


def subtitulo(texto):
    print(COR_TITULO + f"\n  ── {texto} ──\n")


def dialogo(nome_npc, texto):
    print(COR_NPC + Style.BRIGHT + f"\n  [{nome_npc}]: " + COR_DIALOGO + f'"{texto}"')


def narrar(texto, velocidade=0.04):
    """Print lento, letra por letra"""
    print()
    for char in texto:
        sys.stdout.write(COR_DIALOGO + char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print(COR_NORMAL)


def aviso(texto):
    print(COR_AVISO + f"  ⚠ {texto}")


def erro(texto):
    print(COR_ERRO + f"  ✗ {texto}")


def sucesso(texto):
    print(COR_CURA + f"  ✓ {texto}")


def info_ouro(quantidade):
    print(COR_OURO + f"  💰 {quantidade} ouro")


def info_xp(quantidade):
    print(COR_XP + f"  ✦ +{quantidade} XP")


def info_item(texto):
    print(COR_ITEM + f"  ◆ {texto}")


def info_dano(texto):
    print(COR_DANO + f"  ⚔ {texto}")


def info_cura(texto):
    print(COR_CURA + f"  ♥ {texto}")


def menu(opcoes):
    """Mostra menu numerado. opcoes = lista de strings"""
    print()
    for i, op in enumerate(opcoes, 1):
        print(COR_MENU + f"  [{i}] {op}")
    print()


def escolha(prompt="> ", validas=None):
    """Lê input do jogador. Se validas, repete até receber valor válido."""
    while True:
        resp = input(COR_MENU + Style.BRIGHT + f"  {prompt}" + COR_NORMAL).strip()
        if validas is None or resp in validas:
            return resp
        erro("Opção inválida! Tente novamente.")


def barra_hp(nome, hp, hp_max, is_enemy=False):
    """Mostra barra de HP visual"""
    pct = max(0, hp / hp_max)
    preenchido = int(pct * 20)
    vazio = 20 - preenchido

    if pct > 0.6:
        cor = Fore.GREEN
    elif pct > 0.3:
        cor = Fore.YELLOW
    else:
        cor = Fore.RED

    barra = cor + "█" * preenchido + Fore.LIGHTBLACK_EX + "░" * vazio
    label_cor = COR_DANO if is_enemy else Fore.LIGHTCYAN_EX
    print(f"  {label_cor}{nome:.<20s} {barra} {cor}{hp}/{hp_max} HP")


def barra_mana(nome, mana, mana_max):
    if mana_max <= 0:
        return
    pct = max(0, mana / mana_max)
    preenchido = int(pct * 20)
    vazio = 20 - preenchido
    barra = COR_MANA + "█" * preenchido + Fore.LIGHTBLACK_EX + "░" * vazio
    print(f"  {COR_MANA}{'Mana':.<20s} {barra} {COR_MANA}{mana}/{mana_max} MP")


def mostrar_status(player):
    limparUI()

    """Mostra status completo do jogador"""
    titulo(f"STATUS — {player.nome}")
    print(COR_MENU + f"  Classe: {COR_ITEM}{player.classe}")
    print(COR_MENU + f"  Nível:  {COR_XP}{player.lvl}")
    print(COR_MENU + f"  XP:     {COR_XP}{player.XP}/{player.lvl * 60}")
    print(COR_MENU + f"  Ouro:   {COR_OURO}{player.ouro}")
    print()
    barra_hp(player.nome, player.hp, player.hp_max)
    barra_mana(player.nome, player.mana, player.mana_max)
    print()
    print(COR_MENU + f"  Ataque Total:  {COR_DANO}{player.get_ataque_total()}")
    print(COR_MENU + f"  Defesa Total:  {COR_CURA}{player.get_defesa_total()}")

    if player.habilidade_nome:
        print(COR_MENU + f"  Habilidade:    {COR_XP}{player.habilidade_nome} ({player.habilidade_dano} dano, {player.habilidade_custo} mana)")

    print()
    print(COR_MENU + "  ── Equipamento ──")
    for slot, item in player.equipamento.items():
        nome_item = item["nome"] if item else "—"
        print(COR_MENU + f"    {slot:>6s}: {COR_ITEM}{nome_item}")
    separador()


def tela_vitoria():
    limparUI()

    print()
    separador("★")
    print(COR_OURO + Style.BRIGHT + """
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║      🏆  V I T Ó R I A  ! ! !  🏆       ║
    ║                                          ║
    ║   Você derrotou Morvak e salvou Lyris!   ║
    ║                                          ║
    ║   A paz retorna às terras e seu nome     ║
    ║   será lembrado por todas as eras.       ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """)
    separador("★")


def tela_derrota():
    limparUI()

    print()
    separador("†")
    print(COR_ERRO + Style.BRIGHT + """
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║     💀  G A M E   O V E R  💀           ║
    ║                                          ║
    ║   Sua jornada chegou ao fim...           ║
    ║   Mas a escuridão nunca esquece.         ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """)
    separador("†")


def tela_titulo():
    limparUI()

    print(COR_BOSS + Style.BRIGHT + """
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║   ⚔️  L E N D A S   D E   L Y R I S  ⚔️        ║
    ║                                                  ║
    ║          ░▒▓ A Torre de Morvak ▓▒░               ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    """)
    print(COR_DIALOGO + "         Um RPG de texto em Python\n")
