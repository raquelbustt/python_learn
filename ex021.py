import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('')
pygame.mixer.music.play(loops=0, start=0)
pygame.event.wait()