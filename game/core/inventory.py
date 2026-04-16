# game/core/inventory.py

from game.core.ui import (
    titulo, subtitulo, menu, escolha, info_item, aviso, erro, limparUI, 
    sucesso, separador, COR_ITEM, COR_MENU, COR_OURO, COR_NORMAL
)


def mostrar_inventario(player):
    """Exibe o inventário completo do jogador"""
    titulo(f"INVENTÁRIO — {player.nome}")

    if not player.inventario:
        aviso("Seu inventário está vazio.")
        separador()
        return

    for i, item in enumerate(player.inventario, 1):
        tipo = item.get("tipo", "???")
        nome = item.get("nome", "???")
        nivel = item.get("nivel", "?")
        detalhes = _detalhes_item(item)
        print(COR_MENU + f"  [{i}] " + COR_ITEM + f"{nome}" + COR_MENU + f" (Lvl {nivel} | {tipo}) {detalhes}")

    print(COR_OURO + f"\n  💰 Ouro: {player.ouro}")
    separador()


def _detalhes_item(item):
    """Retorna string com stats do item"""
    partes = []
    if "ataque" in item:
        partes.append(f"ATK +{item['ataque']}")
    if "defesa" in item:
        partes.append(f"DEF +{item['defesa']}")
    if "magia" in item:
        partes.append(f"MAG +{item['magia']}")
    if "destreza" in item:
        partes.append(f"DEX +{item['destreza']}")
    if "cura" in item:
        partes.append(f"Cura {item['cura']} HP")
    if "mana" in item:
        partes.append(f"Restaura {item['mana']} MP")
    if "preco" in item:
        partes.append(f"💰{item['preco']}")
    return "| " + " | ".join(partes) if partes else ""


def menu_inventario(player):
    limparUI()

    """Menu interativo do inventário"""
    while True:
        mostrar_inventario(player)

        menu(["Equipar item", "Usar item", "Descartar item", "Voltar"])
        op = escolha(validas=["1", "2", "3", "4"])

        if op == "1":
            equipar_item_menu(player)
        elif op == "2":
            usar_item_menu(player)
        elif op == "3":
            descartar_item_menu(player)
        elif op == "4":
            break


def equipar_item_menu(player):
    """Menu para equipar um item"""
    equipaveis = [(i, item) for i, item in enumerate(player.inventario)
                  if item.get("tipo") in ("arma", "armadura")]

    if not equipaveis:
        aviso("Nenhum item equipável no inventário.")
        return

    subtitulo("EQUIPAR ITEM")
    for idx, (i, item) in enumerate(equipaveis, 1):
        detalhes = _detalhes_item(item)
        print(COR_MENU + f"  [{idx}] " + COR_ITEM + f"{item['nome']} " + COR_MENU + detalhes)

    print(COR_MENU + f"  [0] Cancelar")
    op = escolha()

    try:
        num = int(op)
        if num == 0:
            return
        if 1 <= num <= len(equipaveis):
            _, item = equipaveis[num - 1]
            ok, msg = player.equipar(item)
            if ok:
                sucesso(msg)
            else:
                erro(msg)
        else:
            erro("Opção inválida.")
    except ValueError:
        erro("Digite um número.")


def usar_item_menu(player):
    """Menu para usar consumível"""
    consumiveis = [(i, item) for i, item in enumerate(player.inventario)
                   if item.get("tipo") == "consumivel"]

    if not consumiveis:
        aviso("Nenhum consumível no inventário.")
        return

    subtitulo("USAR ITEM")
    for idx, (i, item) in enumerate(consumiveis, 1):
        detalhes = _detalhes_item(item)
        print(COR_MENU + f"  [{idx}] " + COR_ITEM + f"{item['nome']} " + COR_MENU + detalhes)

    print(COR_MENU + f"  [0] Cancelar")
    op = escolha()

    try:
        num = int(op)
        if num == 0:
            return
        if 1 <= num <= len(consumiveis):
            _, item = consumiveis[num - 1]
            ok, msg = player.usar_item(item)
            if ok:
                sucesso(msg)
            else:
                erro(msg)
        else:
            erro("Opção inválida.")
    except ValueError:
        erro("Digite um número.")


def descartar_item_menu(player):
    """Menu para descartar item"""
    if not player.inventario:
        aviso("Inventário vazio.")
        return

    subtitulo("DESCARTAR ITEM")
    for i, item in enumerate(player.inventario, 1):
        print(COR_MENU + f"  [{i}] " + COR_ITEM + f"{item['nome']}")

    print(COR_MENU + f"  [0] Cancelar")
    op = escolha()

    try:
        num = int(op)
        if num == 0:
            return
        if 1 <= num <= len(player.inventario):
            item = player.inventario.pop(num - 1)
            aviso(f"Você descartou {item['nome']}.")
        else:
            erro("Opção inválida.")
    except ValueError:
        erro("Digite um número.")


def usar_item_combate(player):
    """Menu simplificado para usar item durante combate. Retorna True se usou."""
    consumiveis = [(i, item) for i, item in enumerate(player.inventario)
                   if item.get("tipo") == "consumivel"]

    if not consumiveis:
        aviso("Nenhum consumível disponível!")
        return False

    subtitulo("USAR ITEM")
    for idx, (i, item) in enumerate(consumiveis, 1):
        detalhes = _detalhes_item(item)
        print(COR_MENU + f"  [{idx}] " + COR_ITEM + f"{item['nome']} " + COR_MENU + detalhes)

    print(COR_MENU + f"  [0] Cancelar")
    op = escolha()

    try:
        num = int(op)
        if num == 0:
            return False
        if 1 <= num <= len(consumiveis):
            _, item = consumiveis[num - 1]
            ok, msg = player.usar_item(item)
            if ok:
                sucesso(msg)
                return True
            else:
                erro(msg)
                return False
        else:
            erro("Opção inválida.")
            return False
    except ValueError:
        erro("Digite um número.")
        return False
