import random


class Player:
    def __init__(self, nome):
        self.nome = nome
        self.classe = ""
        self.hp = 100
        self.hp_max = 100
        self.critPerc = 0
        self.critMult = 0
        self.mana = 0
        self.mana_max = 0
        self.ataque = 10
        self.defesa = 5
        self.magia = 0
        self.destreza = 0
        self.XP = 0
        self.lvl = 1
        self.ouro = 30
        self.inventario = []  # lista de dicts (itens)
        self.equipamento = {
            "arma": None,
            "head": None,
            "chest": None,
            "legs": None,
        }
        self.capitulo = 1  # progresso da história
        self.vitorias_floresta = 0
        self.vitorias_caverna = 0
        self.habilidade_nome = ""
        self.habilidade_dano = 0
        self.habilidade_custo = 0

    def esta_vivo(self):
        return self.hp > 0

    def receberXP(self, xp_ganho):
        self.XP += xp_ganho
        xp_para_subir = self.lvl * 60
        if self.XP >= xp_para_subir:
            self.XP -= xp_para_subir
            self.subir_nivel()
            return True
        return False

    def subir_nivel(self):
        self.lvl += 1
        bonus_hp = random.randint(10, 20)
        bonus_atk = random.randint(3, 8)
        bonus_def = random.randint(2, 5)
        self.hp_max += bonus_hp
        self.hp = self.hp_max
        self.ataque += bonus_atk
        self.defesa += bonus_def
        self.critPerc *= 1.2
        self.critMult *= 1.2
        if self.mana_max > 0:
            self.mana_max += random.randint(5, 15)
            self.mana = self.mana_max
        if self.habilidade_dano > 0:
            self.habilidade_dano += random.randint(3, 8)

    def get_ataque_total(self):
        total = self.ataque
        arma = self.equipamento.get("arma")
        if arma:
            total += arma.get("ataque", 0)
            total += arma.get("magia", 0)
            total += arma.get("destreza", 0)
        return total

    def get_defesa_total(self):
        total = self.defesa
        for slot in ["head", "chest", "legs"]:
            peca = self.equipamento.get(slot)
            if peca:
                total += peca.get("defesa", 0)
        return total

    def equipar(self, item):
        """Equipa item do inventário. Retorna (sucesso, mensagem)"""
        tipo = item.get("tipo")

        if tipo == "arma":
            slot = "arma"
        elif tipo == "armadura":
            slot = item.get("slot")
        else:
            return False, "Este item não pode ser equipado."

        # Verificar classe
        classes_permitidas = item.get("classe", [])
        if classes_permitidas and self.classe.lower() not in classes_permitidas:
            return False, f"Somente {', '.join(classes_permitidas)} podem usar isso."

        # Desequipar atual
        atual = self.equipamento.get(slot)
        if atual:
            self.inventario.append(atual)

        # Equipar novo
        self.equipamento[slot] = item
        if item in self.inventario:
            self.inventario.remove(item)
        return True, f"{item['nome']} equipado no slot '{slot}'!"

    def usar_item(self, item):
        """Usa um consumível. Retorna (sucesso, mensagem)"""
        if item.get("tipo") != "consumivel":
            return False, "Este item não é consumível."

        msgs = []
        if "cura" in item:
            cura = item["cura"]
            self.hp = min(self.hp + cura, self.hp_max)
            msgs.append(f"Recuperou {cura} HP! (HP: {self.hp}/{self.hp_max})")

        if "mana" in item:
            mana = item["mana"]
            self.mana = min(self.mana + mana, self.mana_max)
            msgs.append(f"Recuperou {mana} Mana! (Mana: {self.mana}/{self.mana_max})")

        if item in self.inventario:
            self.inventario.remove(item)

        return True, " | ".join(msgs) if msgs else "Item usado."

    def adicionar_item(self, item):
        self.inventario.append(item)

    def remover_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            return True
        return False

    def descansar(self):
        self.hp = self.hp_max
        self.mana = self.mana_max
