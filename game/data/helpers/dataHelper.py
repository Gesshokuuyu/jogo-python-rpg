import random
from game.data.data import ARMAS, ARMADURAS, CONSUMIVEIS, INIMIGOS, MERCADORES


# =========================
# BASE
# =========================

def _get_all_items():
    """Retorna todos os itens juntos"""
    return {
        **ARMAS,
        **ARMADURAS,
        **CONSUMIVEIS
    }


# =========================
# BUSCA SIMPLES
# =========================

def get_item_by_id(item_id):
    """Busca item pelo ID, retorna cópia com o id incluso"""
    item = _get_all_items().get(item_id)
    if item:
        copia = dict(item)
        copia["id"] = item_id
        return copia
    return None


def exists(item_id):
    """Verifica se item existe"""
    return item_id in _get_all_items()


# =========================
# FILTROS
# =========================

def get_by_tipo(tipo):
    """Filtra por tipo: arma, armadura, consumivel"""
    return {
        k: v for k, v in _get_all_items().items()
        if v.get("tipo") == tipo
    }


def get_by_classe(classe):
    """Itens utilizáveis por uma classe"""
    resultado = {}
    for k, v in _get_all_items().items():
        if "classe" in v and classe in v["classe"]:
            resultado[k] = v
        elif "classe" not in v:
            resultado[k] = v
    return resultado


def get_by_nivel(nivel):
    """Filtra por nível"""
    return {
        k: v for k, v in _get_all_items().items()
        if v.get("nivel") == nivel
    }


def get_by_slot(slot):
    """Filtra armaduras por slot (head, chest, legs)"""
    return {
        k: v for k, v in _get_all_items().items()
        if v.get("slot") == slot
    }


# =========================
# BUSCA AVANÇADA
# =========================

def search(nome=None, tipo=None, classe=None, nivel=None, slot=None):
    """Busca combinada com qualquer parâmetro"""
    resultado = {}

    for k, v in _get_all_items().items():
        if nome and nome.lower() not in v.get("nome", "").lower():
            continue
        if tipo and v.get("tipo") != tipo:
            continue
        if classe and classe not in v.get("classe", []):
            continue
        if nivel and v.get("nivel") != nivel:
            continue
        if slot and v.get("slot") != slot:
            continue
        resultado[k] = v

    return resultado


# =========================
# INIMIGOS
# =========================

def get_enemy_data(enemy_id):
    """Retorna dados de um inimigo pelo ID"""
    return INIMIGOS.get(enemy_id)


def get_loot(enemy_id):
    """Roda tabela de loot de um inimigo, retorna lista de itens dropados"""
    enemy_data = INIMIGOS.get(enemy_id)
    if not enemy_data:
        return []

    drops = []
    for entry in enemy_data.get("loot", []):
        roll = random.randint(1, 100)
        if roll <= entry["chance"]:
            item = get_item_by_id(entry["item_id"])
            if item:
                drops.append(item)
    return drops


# =========================
# MERCADORES
# =========================

def get_merchant(merchant_id):
    """Retorna dados do mercador"""
    return MERCADORES.get(merchant_id)


def get_merchant_items(merchant_id):
    """Retorna lista de itens à venda pelo mercador"""
    merchant = MERCADORES.get(merchant_id)
    if not merchant:
        return []

    itens = []
    for item_id in merchant.get("itens", []):
        item = get_item_by_id(item_id)
        if item:
            itens.append(item)
    return itens


# =========================
# UTILITÁRIOS
# =========================

def listar_todos():
    return _get_all_items()


def listar_ids():
    return list(_get_all_items().keys())


def pretty_print(items):
    """Print bonito (debug)"""
    for k, v in items.items():
        print(f"[{k}] {v.get('nome')} (lvl {v.get('nivel')})")