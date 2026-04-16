# game/core/sound.py
# Wrapper para sons com pygame.mixer
# Se pygame não estiver instalado, o jogo funciona normalmente sem som.

_sound_available = False

try:
    import pygame
    pygame.mixer.init()
    _sound_available = True
except Exception:
    pass


def tocar_efeito(arquivo):
    """Toca um efeito sonoro (arquivo .wav/.ogg)"""
    if not _sound_available:
        return
    try:
        som = pygame.mixer.Sound(arquivo)
        som.play()
    except Exception:
        pass


def tocar_musica(arquivo, loop=True):
    """Toca música de fundo"""
    if not _sound_available:
        return
    try:
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play(-1 if loop else 0)
    except Exception:
        pass


def parar_musica():
    """Para a música de fundo"""
    if not _sound_available:
        return
    try:
        pygame.mixer.music.stop()
    except Exception:
        pass


def som_disponivel():
    """Retorna True se o sistema de som está disponível"""
    return _sound_available
