import pygame

from constants import DEFAULT_FONT, DEFAULT_FONT_SIZE, DISPLAY_WIDTH, DISPLAY_HEIGHT, CENTER_W, CENTER_H, \
    DEFAULT_FONT_COLOR


class SetUpClass:
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))  # init window
    pygame.display.set_caption("Fulminant Reader")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    def init_font(self, font=DEFAULT_FONT, size=DEFAULT_FONT_SIZE):
        pygame.font.init()
        self.font = pygame.font.SysFont(font, size)

    def center_text(self, text):
        return text.get_rect(center=(CENTER_W, CENTER_H))

    def show_text(self, text, color=DEFAULT_FONT_COLOR):
        text = self.font.render(f"{text}", 1, color)
        self.screen.blit(text, self.center_text(text))
        return pygame.display.update()
