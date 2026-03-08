# =================================
# Exercício 21 - Tocar música com pygame
# =================================

# -------- Minha solução --------
# Caminho hardcoded da máquina local — não portável
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/home/usuario/python/curso1 guanabara/testes/scripts-python/music.mp3')
pygame.mixer.music.play()
input("Pressione Enter para sair enquanto a música toca...")


# -------- Solução corrigida --------
# Usar caminho relativo: coloque music.mp3 na mesma pasta do script
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')  # arquivo na mesma pasta
pygame.mixer.music.play()
input('Pressione Enter para parar a música...')
pygame.mixer.music.stop()
pygame.quit()
