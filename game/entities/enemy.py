class Enemy:
    def __init__(self, nome, hp, ataque, xp):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.qtd_XP = xp

    def esta_vivo(self):
        return self.hp > 0