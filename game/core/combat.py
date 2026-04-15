# game/combat.py

from game.entities.player import Player
from game.entities.enemy import Enemy

import random 

def iniciar_combate(player, enemy):
    if(isinstance(player, Player) and isinstance(enemy, Enemy)):

        print(f"\n Se prepare para o comabte contra {enemy.nome}\n")

        while player.esta_vivo() and enemy.esta_vivo():
            print(f"{player.nome} HP: {player.hp}")
            print(f"{enemy.nome} HP: {enemy.hp}")

            acao = input("1 - Atacar | 2 - Fugir\n> ")

            if acao == "1":
                enemy.hp -= player.ataque
                print(f"Você causou {player.ataque} de dano!")

                if enemy.esta_vivo():
                    player.hp -= enemy.ataque
                    print(f"{enemy.nome} causou {enemy.ataque} de dano!")

            elif acao == "2":
                print("Você fugiu!")
                return
            
            else :
                randomDamage = random.random(1, 10)
                print(f"Você não se decidiu e tomou {randomDamage} de {enemy.nome}")

        if player.esta_vivo():
            print("Você venceu!")
            player.receberXP(enemy.qtd_XP)
            return True
        else:
            print("Você foi derrotado...")
            return False
    else: 
        print("O jogo foi mal iniciado, reinicie")
        quit()