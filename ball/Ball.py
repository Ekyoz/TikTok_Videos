import pygame
import settings

class Ball:
    def __init__(self, color, x_offset = 0, y_offset = 0, vx = 0, vy = 0):
        self.x = settings.WIDTH / 2 - x_offset
        self.y = settings.HEIGHT / 2 - y_offset
        self.radius = settings.RADIUS_BALL
        self.color = color
        self.vx = vx
        self.vy = vy
        self.screen_width = settings.WIDTH
        self.screen_height = settings.HEIGHT

        self.gravity = settings.GRAVITY
        self.bounce = settings.BOUNCE_BALL

    def update(self):
        # Appliquer la gravité à la vitesse verticale
        self.vy += self.gravity

        # Met à jour la position
        self.x += self.vx
        self.y += self.vy

        # Rebond horizontal
        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen_width:
            self.vx *= -1
            self.x = max(self.radius, min(self.x, self.screen_width - self.radius))

        # Rebond vertical (avec amortissement)
        if self.y + self.radius >= self.screen_height:
            self.vy *= -self.bounce
            self.y = self.screen_height - self.radius

        # Empêche de sortir par le haut
        if self.y - self.radius <= 0:
            self.vy *= -1
            self.y = self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
