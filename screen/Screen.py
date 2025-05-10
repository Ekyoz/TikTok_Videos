import pygame
import settings


class Screen:
    _instance = None
    _screen = None

    def __new__(cls):
        # Singleton : toujours la même instance
        if cls._instance is None:
            cls._instance = super(Screen, cls).__new__(cls)
            cls._instance._init_screen()
        return cls._screen

    def _init_screen(self):
        flags = pygame.FULLSCREEN if getattr(settings, "FULLSCREEN", False) else 0
        size = (settings.WIDTH, settings.HEIGHT)

        # Crée la surface principale
        Screen._screen = pygame.display.set_mode(size, flags)

        # Définir un titre
        if hasattr(settings, "TITLE"):
            pygame.display.set_caption(settings.TITLE)

        # Définir une icône
        if hasattr(settings, "ICON_PATH") and settings.ICON_PATH:
            try:
                icon = pygame.image.load(settings.ICON_PATH)
                pygame.display.set_icon(icon)
            except pygame.error:
                print(f"Erreur : impossible de charger l'icône '{settings.ICON_PATH}'")

    @classmethod
    def get(cls):
        """Retourne l'objet screen Pygame."""
        return cls._screen

    @classmethod
    def clear(cls, color=None):
        """Efface l'écran avec la couleur donnée (par défaut : settings.BG_COLOR)."""
        if color is None:
            color = getattr(settings, "BG_COLOR", (0, 0, 0))
        cls._screen.fill(color)
