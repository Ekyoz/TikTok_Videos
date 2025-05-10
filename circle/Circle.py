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

        # Si la balle est exactement au centre (éviter division par zéro)
        if dist == 0:
            return

        # Calcul de l'angle de la balle par rapport au centre
        angle_to_ball = math.atan2(dy, dx) % (2 * math.pi)

        # Vérifie si la balle est dans la portion d'arc
        start = self.start_angle % (2 * math.pi)
        end = self.end_angle % (2 * math.pi)

        in_arc = False
        if start < end:
            in_arc = start <= angle_to_ball <= end
        else:
            in_arc = angle_to_ball >= start or angle_to_ball <= end

        if not in_arc:
            return  # pas dans la zone de collision active

        # Calcul de la distance à la surface du cercle
        penetration = self.radius - dist

        # Collision extérieure
        if dist > self.radius - ball.radius and dist < self.radius + ball.radius:
            nx = dx / dist
            ny = dy / dist

            # Réflexion
            dot = ball.vx * nx + ball.vy * ny
            ball.vx -= 2 * dot * nx
            ball.vy -= 2 * dot * ny

            # Appliquer rebond
            ball.vx *= self.bounce
            ball.vy *= self.bounce

            # Repositionnement correct
            ball.x += nx * (ball.radius - penetration)
            ball.y += ny * (ball.radius - penetration)

        # Collision intérieure
        elif dist < self.radius - ball.radius:
            nx = -dx / dist
            ny = -dy / dist

            # Réflexion
            dot = ball.vx * nx + ball.vy * ny
            ball.vx -= 2 * dot * nx
            ball.vy -= 2 * dot * ny

            ball.vx *= self.bounce
            ball.vy *= self.bounce

            # Repositionnement vers l'intérieur
            ball.x += nx * (ball.radius + penetration)
            ball.y += ny * (ball.radius + penetration)



