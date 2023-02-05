import pygame
from constantes import *
from tabuleiro import Tabuleiro

# Inicialização
pygame.init()

# Setup
janela = pygame.display.set_mode((ALTURA, LARGURA))
fundo_temp = pygame.image.load("Fundo.png")
fundo_tamanho = fundo_temp.get_size()
fundo_razao = LARGURA / fundo_tamanho[0], ALTURA / fundo_tamanho[1]
novo_tamanho = fundo_tamanho[0] * fundo_razao[0], fundo_tamanho[1] * fundo_razao[1]
fundo = pygame.transform.scale(fundo_temp, novo_tamanho)

tabuleiro = Tabuleiro()
relogio = pygame.time.Clock()

# Funções
def update():
    mouse_pos = pygame.mouse.get_pos()
    tabuleiro.atualizar_mouse(mouse_pos)

def desenhar():
    janela.blit(fundo, (0, 0))
    tabuleiro.desenhar(janela)
    pygame.display.update()

# Loop
def jogo():
    pygame.display.set_caption("Jogo da Velha!!")

    rodando = True
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()

                if mouse_button[0]:
                    tabuleiro.quando_clicado(mouse_pos)
        
        update()
        desenhar()

    pygame.quit()

jogo()
