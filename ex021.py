# 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer_music.load('''nome do arquivo''')
pygame.mixer_music.play()
pygame.event.wait()