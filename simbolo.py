import pygame
from constantes import *


class Simbolo:
    def __init__(self, x, y, simbolo, surface=None):
        self.x = x
        self.y = y
        self.simbolo = simbolo
        
        if surface is not None:
            self.img = surface
        elif simbolo == SIMBOLO_O:
            self.img = pygame.image.load("Circulo.png").convert_alpha()
        else:
            self.img = pygame.image.load("X.png").convert_alpha()
        
        self.tamanho = self.img.get_size()
        self.mini_img = pygame.transform.scale(self.img, (self.tamanho[0] * 0.5, self.tamanho[1] * 0.5))
        self.mini_tamanho = self.mini_img.get_size()
    
    def desenhar_traço(self, janela, mx, my):
        pos_ajustada = mx - self.mini_tamanho[0] // 2, my - self.mini_tamanho[1] // 2 # Posição com ajuste para centralização

        janela.blit(self.mini_img, pos_ajustada)

    def desenhar(self, janela):
        pos_abs = self.x * TAMANHO_CASA, self.y * TAMANHO_CASA  # Posição absoluta
        pos_ajustada = pos_abs[0] + (TAMANHO_CASA - self.tamanho[0]) // 2, pos_abs[1] + (TAMANHO_CASA - self.tamanho[1]) / 2 # Posição com ajuste para centralização

        janela.blit(self.img, pos_ajustada)
    
    def copy(self, x, y):
        return Simbolo(x, y, self.simbolo, self.img.copy())
