from game.data.data import INIMIGOS


class Enemy:
    def __init__(self, enemy_id):
        data = INIMIGOS.get(enemy_id)
        if not data:
            raise ValueError(f"Inimigo '{enemy_id}' não encontrado nos dados!")

        self.enemy_id = enemy_id
        self.nome = data["nome"]
        self.hp = data["hp"]
        self.hp_max = data["hp"]
        self.ataque = data["ataque"]
        self.defesa = data.get("defesa", 0)
        self.qtd_XP = data["xp"]
        self.ouro = data.get("ouro", 0)
        self.is_boss = data.get("is_boss", False)

    def esta_vivo(self):
        return self.hp > 0