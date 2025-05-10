import pygame
import math
import settings

class Circle:
    def __init__(self, start_angle=0, end_angle=360):
        self.x = settings.WIDTH / 2
        self.y = settings.HEIGHT / 2
        self.width = settings.WIDTH_CIRCLE
        self.radius = settings.RADIUS_CIRCLE
        self.color = settings.COLOR_CIRCLE
        self.start_angle = math.radians(start_angle)
        self.end_angle = math.radians(end_angle)
        self.bounce = settings.BOUNCE_CIRCLE

    def draw(self, screen):
        # On peut dessiner un cercle complet ou un arc
        if self.start_angle == 0 and self.end_angle >= 2 * math.pi:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, self.width)
        else:
            rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
            pygame.draw.arc(screen, self.color, rect, self.start_angle, self.end_angle, self.width)

    def check_collision(self, ball):
        dx = ball.x - self.x
        dy = ball.y - self.y
        dist = math.hypot(dx, dy)
        nx = ny = 0

        # Collision intérieure : balle à l'intérieur du cercle
        if dist + ball.radius >= self.radius:
            # Normale pointant vers l'extérieur du cercle
            nx = -dx / dist
            ny = -dy / dist

        # Produit scalaire pour projeter la vitesse sur la normale
        dot = ball.vx * nx + ball.vy * ny

        # Réflexion : inverse la vitesse suivant la direction normale
        ball.vx -= 2 * dot * nx
        ball.vy -= 2 * dot * ny

        # Appliquer rebond (en fonction de la direction)
        ball.vx *= self.bounce
        ball.vy *= self.bounce

        # Repositionner légèrement la balle pour éviter qu'elle reste coincée
        overlap = (dist + ball.radius) - self.radius if dist + ball.radius <= self.radius else (dist - ball.radius) - self.radius
        ball.x -= nx * overlap
        ball.y -= ny * overlap


