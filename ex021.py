import pygame

pygame.init()
pygame.mixer.music.load('Cat_Stevens_-_Wild_World.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()