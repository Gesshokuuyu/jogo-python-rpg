# game/core/merchant.py

from game.data.helpers.dataHelper import get_merchant, get_merchant_items
from game.core.ui import (
    titulo, subtitulo, dialogo, menu, escolha, info_item, info_ouro,
    aviso, erro, sucesso, separador, COR_ITEM, COR_MENU, COR_OURO, COR_NORMAL
)
from game.core.inventory import _detalhes_item


def abrir_loja(player, merchant_id):
    """Abre a loja de um mercador"""
    merchant = get_merchant(merchant_id)
    if not merchant:
        erro("Mercador não encontrado!")
        return

    dialogo(merchant["nome"], merchant["saudacao"])

    while True:
        titulo(f"LOJA — {merchant['nome']}")
        print(COR_OURO + f"  Seu ouro: {player.ouro}\n")

        menu(["Comprar", "Vender", "Sair da loja"])
        op = escolha(validas=["1", "2", "3"])

        if op == "1":
            _comprar(player, merchant_id, merchant["nome"])
        elif op == "2":
            _vender(player, merchant["nome"])
        elif op == "3":
            dialogo(merchant["nome"], "Volte sempre, aventureiro!")
            break


def _comprar(player, merchant_id, nome_merchant):
    """Menu de compra"""
    itens = get_merchant_items(merchant_id)
    if not itens:
        aviso("Nenhum item à venda.")
        return

    subtitulo("COMPRAR")
    for i, item in enumerate(itens, 1):
        preco = item.get("preco", 0)
        detalhes = _detalhes_item(item)
        acessivel = "✓" if player.ouro >= preco else "✗"
        print(COR_MENU + f"  [{i}] " + COR_ITEM + f"{item['nome']}" +
              COR_OURO + f" — {preco} ouro " +
              COR_MENU + f"[{acessivel}] {detalhes}")

    print(COR_MENU + f"  [0] Voltar")
    op = escolha()

    try:
        num = int(op)
        if num == 0:
            return
        if 1 <= num <= len(itens):
            item = itens[num - 1]
            preco = item.get("preco", 0)
            if player.ouro >= preco:
                player.ouro -= preco
                player.adicionar_item(dict(item))  # cópia
                sucesso(f"Comprou {item['nome']} por {preco} ouro!")
                info_ouro(f"Ouro restante: {player.ouro}")
            else:
                erro("Ouro insuficiente!")
        else:
            erro("Opção inválida.")
    except ValueError:
        erro("Digite um número.")


def _vender(player, nome_merchant):
    """Menu de venda (50% do preço)"""
    if not player.inventario:
        aviso("Seu inventário está vazio.")
        return

    subtitulo("VENDER (50% do valor)")
    for i, item in enumerate(player.inventario, 1):
        preco = item.get("preco", 0)
        valor_venda = preco // 2
        print(COR_MENU + f"  [{i}] " + COR_ITEM + f"{item['nome']}" +
              COR_OURO + f" — {valor_venda} ouro")

    print(COR_MENU + f"  [0] Voltar")
    op = escolha()

    try:
        num = int(op)
        if num == 0:
            return
        if 1 <= num <= len(player.inventario):
            item = player.inventario.pop(num - 1)
            preco = item.get("preco", 0)
            valor = preco // 2
            player.ouro += valor
            sucesso(f"Vendeu {item['nome']} por {valor} ouro!")
            info_ouro(f"Ouro total: {player.ouro}")
        else:
            erro("Opção inválida.")
    except ValueError:
        erro("Digite um número.")
