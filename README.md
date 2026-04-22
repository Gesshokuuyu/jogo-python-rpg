
<h1 align="center">⚔️ Jogo Python RPG</h1>

<p align="center">
  <em>Um RPG de terminal com narrativa, combate por turnos, inventário, mercadores e um chefão final.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/colorama-terminal%20colorido-brightgreen" />
  <img src="https://img.shields.io/badge/pygame-som%20e%20música-orange" />
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" />
</p>

---

## 📖 Sobre o Jogo

Você é um aventureiro que chega à **Vila de Lyris**, uma pequena comunidade cercada por florestas sombrias. Os moradores sussurram sobre uma torre escura no horizonte — e sobre **Morvak, o Senhor das Sombras**, que ameaça destruir tudo.

Escolha sua classe, explore os arredores, derrote inimigos, compre equipamentos e siga a narrativa até o confronto final na **Torre de Morvak**.

---

## 🎮 Funcionalidades

- 🗺️ **Narrativa progressiva** com 3 capítulos e áreas desbloqueáveis
- ⚔️ **Combate por turnos** com ataques, habilidades especiais e uso de itens
- 🧙 **3 classes jogáveis** com atributos e equipamentos distintos
- 🎒 **Inventário completo** com sistema de equipamentos por slot
- 🛒 **Mercadores** nas diferentes áreas do mapa
- 💰 **Sistema de loot** com chances por inimigo
- 📈 **Level up** com ganho de XP e melhora de atributos
- 🔊 **Efeitos sonoros e música** via pygame
- 🎨 **Interface colorida no terminal** via colorama

---

## 🧝 Classes

| Classe      | HP  | Mana | ATK | DEF | Habilidade Especial     |
|-------------|-----|------|-----|-----|--------------------------|
| ⚔️ Guerreiro | 120 | 20   | 12  | 8   | Golpe Brutal (25 dmg)    |
| 🏹 Arqueiro  | 90  | 30   | 9   | 5   | Chuva de Flechas (20 dmg)|
| 🔮 Mago      | 75  | 60   | 5   | 3   | Bola de Fogo (30 dmg)    |

Cada classe começa com uma **arma e armadura exclusivas**, além de **2 Poções de Vida**.

---

## 🗺️ Mapa e Progressão

```
[Vila de Lyris] ── Hub central da aventura
      │
      ├── 🍺 Taverna          → Descanso, inventário, Baldric (mercador)     [Cap. 1+]
      ├── 🌲 Floresta de Lyris → Lobos, Goblins, Criaturas Sombrias          [Cap. 1+]
      ├── 🪨 Caverna das Sombras → Trolls, Esqueletos, Golem (mini-boss)    [Cap. 2+]
      └── 🏰 Torre de Morvak  → Cavaleiros, Espectros, Morvak (boss final)  [Cap. 3+]
```

> As áreas são desbloqueadas conforme você progride na narrativa. Complete a **Floresta** para acessar a Caverna, e derrote o **Golem** para acessar a Torre.

---

## 👾 Inimigos

### 🌲 Floresta de Lyris
| Inimigo            | HP | ATK | DEF | XP | Ouro |
|--------------------|----|-----|-----|----|------|
| Lobo Selvagem      | 35 | 7   | 2   | 15 | 8    |
| Goblin             | 40 | 8   | 3   | 20 | 12   |
| Criatura Sombria   | 50 | 10  | 4   | 30 | 18   |

### 🪨 Caverna das Sombras
| Inimigo            | HP | ATK | DEF | XP | Ouro |
|--------------------|----|-----|-----|----|------|
| Aranha Gigante     | 55 | 11  | 3   | 30 | 15   |
| Esqueleto Guerreiro| 60 | 12  | 8   | 35 | 20   |
| Troll da Caverna   | 80 | 14  | 6   | 45 | 25   |
| 💀 Golem de Pedra  | 150| 18  | 12  | 80 | 60   |

### 🏰 Torre de Morvak
| Inimigo               | HP  | ATK | DEF | XP  | Ouro |
|-----------------------|-----|-----|-----|-----|------|
| Cavaleiro das Trevas  | 90  | 16  | 10  | 50  | 30   |
| Espectro              | 70  | 20  | 5   | 55  | 35   |
| 👑 Morvak             | 300 | 25  | 15  | 200 | 500  |

---

## 🛒 Mercadores

| Mercador        | Localização     | Especialidade                      |
|-----------------|-----------------|------------------------------------|
| Baldric         | Taverna         | Consumíveis e equipamentos Nível 1 |
| Dúrin, o Anão   | Caverna         | Equipamentos Nível 2 e consumíveis |

---

## 🎒 Sistema de Itens

### Armas (por classe e nível)
| Nível | Guerreiro         | Arqueiro        | Mago                  |
|-------|-------------------|-----------------|-----------------------|
| 1     | Espada Básica     | Arco Curto      | Cajado Simples        |
| 2     | Espada de Aço     | Arco Longo      | Cajado de Cristal     |
| 3     | Lâmina Flamejante | Arco do Vento   | Báculo das Sombras    |

### Armaduras
Os slots de armadura são: **Cabeça**, **Peitoral** e **Pernas**. Cada peça tem restrições de classe e bônus próprios.

### Consumíveis
| Item                | Efeito          |
|---------------------|-----------------|
| Poção de Vida       | +30 HP          |
| Poção de Vida Grande| +70 HP          |
| Poção de Mana       | +20 Mana        |
| Elixir de Mana      | +50 Mana        |
| Antídoto            | +10 HP          |

---

## 🚀 Como Jogar

### 1. Pré-requisitos

- Python 3.10 ou superior
- pip

### 2. Clone o repositório

```bash
git clone https://github.com/Gesshokuuyu/jogo-python-rpg.git
cd jogo-python-rpg
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o jogo

```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```
jogo-python-rpg/
├── main.py                  # Ponto de entrada
├── requirements.txt
└── game/
    ├── core/
    │   ├── engine.py        # Inicialização e fluxo principal
    │   ├── classe.py        # Seleção e configuração de classes
    │   ├── combat.py        # Sistema de combate por turnos
    │   ├── inventory.py     # Gerenciamento de inventário
    │   ├── merchant.py      # Lógica de compra/venda
    │   ├── story.py         # Hub da narrativa e fluxo de capítulos
    │   ├── sound.py         # Música e efeitos sonoros
    │   └── ui.py            # Interface visual no terminal
    ├── data/
    │   └── data.py          # Dados de itens, inimigos e mercadores
    ├── entities/
    │   ├── player.py        # Classe do jogador e atributos
    │   └── enemy.py         # Classe dos inimigos
    └── locations/
        ├── tavern.py        # Taverna de Lyris
        ├── forest.py        # Floresta de Lyris
        ├── cave.py          # Caverna das Sombras
        └── tower.py         # Torre de Morvak
```

---

## ⚙️ Dependências

| Biblioteca  | Uso                              |
|-------------|----------------------------------|
| `colorama`  | Coloração e estilo no terminal   |

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

<p align="center">Feito em Python</p>
