import time

import pygame

from application import SetUpClass
from constants import BACKGROUND_COLOR, SPEED, UNPAUSE_DELAY, GREEN, WHITE, START_DELAY, YELLOW


class InitializeReadingApp(SetUpClass):
    flag = True

    async def start(self):
        self.init_font()
        with open("text.txt", "r", encoding="utf8") as self.f:
            for line in self.f:
                for word in line.split():
                    if self.flag is True:
                        self.show_text(word, WHITE)
                        time.sleep(START_DELAY)
                        self.flag = False
                    await self.iterate(word)
                    self.keys_manager()

    async def iterate(self, word):
        self.show_text(word)
        time.sleep(SPEED)
        self.screen.fill((BACKGROUND_COLOR))
        pygame.display.update()

    def pause(self):
        self.show_text(" || Pause")
        self.screen.fill(YELLOW)
        while True:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    self.screen.fill(GREEN)
                    pygame.display.update()
                    time.sleep(UNPAUSE_DELAY)
                    return

    def keys_manager(self):
        # wait for user's action from keyboard
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    quit()
                elif e.key == pygame.K_SPACE:
                    self.pause()
