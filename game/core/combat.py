# game/core/combat.py

import random
from game.core.ui import (
    titulo, subtitulo, menu, escolha, separador,
    barra_hp, barra_mana, info_dano, info_cura, info_xp,
    info_ouro, info_item, aviso, erro, sucesso,limparUI,
    COR_BOSS, COR_DANO, COR_CURA, COR_MENU, COR_XP, COR_ITEM,
    tela_derrota
)
from game.core.inventory import usar_item_combate
from game.data.helpers.dataHelper import get_loot
from colorama import Style


def iniciar_combate(player, enemy):
    """Sistema de combate completo. Retorna True se venceu, False se morreu, None se fugiu."""

    if enemy.is_boss:
        print(COR_BOSS + Style.BRIGHT + f"\n  ☠ BOSS: {enemy.nome} ☠")
    titulo(f"COMBATE — {player.nome} vs {enemy.nome}")

    turno = 1

    while player.esta_vivo() and enemy.esta_vivo():
        subtitulo(f"Turno {turno}")
        barra_hp(player.nome, player.hp, player.hp_max)
        if player.mana_max > 0:
            barra_mana(player.nome, player.mana, player.mana_max)
        barra_hp(enemy.nome, enemy.hp, enemy.hp_max, is_enemy=True)

        opcoes = ["Atacar", "Usar Item", "Fugir"]
        if player.habilidade_nome:
            opcoes.insert(1, f"{player.habilidade_nome} ({player.habilidade_custo} MP)")
        menu(opcoes)

        validas = [str(i) for i in range(1, len(opcoes) + 1)]
        acao = escolha(validas=validas)

        limparUI()

        acao_idx = int(acao)
        jogador_agiu = False

        # Mapear ações dinamicamente
        if acao_idx == 1:
            # Atacar
            jogador_agiu = True
            dano = _calcular_dano(player.get_ataque_total(), enemy.defesa)
            critico = random.random() < 0.15
            if critico:
                dano = int(dano * 1.5)
                info_dano(f"CRÍTICO! Você causou {dano} de dano em {enemy.nome}!")
            else:
                info_dano(f"Você causou {dano} de dano em {enemy.nome}!")
            enemy.hp -= dano

        elif player.habilidade_nome and acao_idx == 2:
            # Habilidade especial
            if player.mana >= player.habilidade_custo:
                jogador_agiu = True
                player.mana -= player.habilidade_custo
                dano = player.habilidade_dano + random.randint(-3, 5)
                info_dano(f"⚡ {player.habilidade_nome}! Causou {dano} de dano!")
                enemy.hp -= dano
            else:
                aviso(f"Mana insuficiente! (Precisa de {player.habilidade_custo} MP)")
                continue

        elif (player.habilidade_nome and acao_idx == 3) or (not player.habilidade_nome and acao_idx == 2):
            # Usar item
            usou = usar_item_combate(player)
            if usou:
                jogador_agiu = True
            else:
                continue

        elif (player.habilidade_nome and acao_idx == 4) or (not player.habilidade_nome and acao_idx == 3):
            # Fugir
            if enemy.is_boss:
                aviso("Não é possível fugir de um Boss!")
                continue
            chance_fuga = random.random()
            if chance_fuga > 0.4:
                aviso("Você fugiu da batalha!")
                return None
            else:
                aviso("Falhou na fuga!")
                jogador_agiu = True  # turno perdido

        # --- TURNO DO INIMIGO ---
        if jogador_agiu and enemy.esta_vivo():
            dano_inimigo = _calcular_dano(enemy.ataque, player.get_defesa_total())
            dano_inimigo = max(1, dano_inimigo)
            player.hp -= dano_inimigo
            info_dano(f"{enemy.nome} causou {dano_inimigo} de dano em você!")

        turno += 1

    # --- RESULTADO ---
    if player.esta_vivo():
        separador("★")
        sucesso(f"Você derrotou {enemy.nome}!")

        # XP
        subiu = player.receberXP(enemy.qtd_XP)
        info_xp(enemy.qtd_XP)
        if subiu:
            print(COR_XP + Style.BRIGHT + f"\n  🎉 LEVEL UP! Agora é nível {player.lvl}!")
            print(COR_MENU + f"  HP: {player.hp_max} | ATK: {player.ataque} | DEF: {player.defesa}")

        # Ouro
        ouro_ganho = enemy.ouro + random.randint(0, 5)
        player.ouro += ouro_ganho
        info_ouro(f"+{ouro_ganho} ouro (Total: {player.ouro})")

        # Loot
        drops = get_loot(enemy.enemy_id)
        if drops:
            subtitulo("LOOT!")
            for item in drops:
                player.adicionar_item(item)
                info_item(f"Obteve: {item['nome']}")
        else:
            aviso("Nenhum item dropado desta vez.")

        separador("★")
        return True
    else:
        tela_derrota()
        return False


def _calcular_dano(ataque, defesa):
    """Calcula dano com variação aleatória e redução de defesa"""
    dano_base = max(1, ataque - defesa // 2)
    variacao = random.randint(-2, 3)
    return max(1, dano_base + variacao)