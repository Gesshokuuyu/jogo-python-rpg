import random

class Player: 
    def __init__(self, nome):
        self.nome = nome
        self.hp = 100
        self.ataque = 10
        self.XP = 0
        self.lvl = 1

    def esta_vivo(self) :
        return self.hp > 0
    
    def receberXP(self, XPToRecive):
        if(self.XP + XPToRecive >= 100):
            self.subir_nivel(self)
            print(f"\n Seu nível subiu para {self.lvl}")
            return
        else:
            self.XP += XPToRecive
            print(f"Você recebeu {XPToRecive} xp e agora esta com {self.XP} de xp")
            return

    def subir_nivel(self):
        self.lvl += 1
        self.ataque += random(5, 15)
        self.hp += self.hp // 2
        self.XP = 0
        return
