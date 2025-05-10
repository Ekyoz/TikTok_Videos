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

        # Determine if the ball is inside or outside the circle
        if dist < self.radius - ball.radius:
            # Ball is inside the circle
            nx = -dx / dist
            ny = -dy / dist
            overlap = (self.radius - ball.radius) - dist
        elif dist > self.radius + ball.radius:
            # Ball is outside the circle
            nx = dx / dist
            ny = dy / dist
            overlap = dist - (self.radius + ball.radius)
        else:
            # Ball is exactly on the boundary; no collision response needed
            return

        # Reflect the velocity along the normal
        dot = ball.vx * nx + ball.vy * ny
        ball.vx -= 2 * dot * nx
        ball.vy -= 2 * dot * ny

        # Apply bounce factor
        ball.vx *= self.bounce
        ball.vy *= self.bounce

        # Reposition ball to avoid sticking
        ball.x += nx * overlap
        ball.y += ny * overlap



