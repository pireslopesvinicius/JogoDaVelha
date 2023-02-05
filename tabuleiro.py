import pygame, random
from constantes import *
from simbolo import Simbolo
from temporizador import Temporizador


class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.circulo = Simbolo(0, 0, SIMBOLO_O)
        self.x = Simbolo(0, 0, SIMBOLO_X)

        self.vez = random.choice([0, 1])  # Escolhe aleatóriamente quem joga primeiro
        self.estado = OCORRENDO
        self.possibilidade = None # Para poder desenhar linha da vitória dependendo de como ganhou

        self.ultima_mouse_pos = None
        self.tempo = Temporizador()

        self.iniciar_tabuleiro()
    
    def iniciar_tabuleiro(self):
        for y in range(LINHAS):
            self.tabuleiro.append([])

            for x in range(COLUNAS):
                self.tabuleiro[y].append(None)
    
    def atualizar_mouse(self, mouse_pos):
        self.ultima_mouse_pos = mouse_pos
    
    def quando_clicado(self, mouse_pos):
        if self.estado == VITORIA:
            self.reiniciar_jogo()
            return
        elif self.estado == EMPATE:
            self.reiniciar_jogo()
            return

        mx, my = mouse_pos[0] // TAMANHO_CASA, mouse_pos[1] // TAMANHO_CASA  # Converte posição do mouse para posição de tabuleiro

        if self.tabuleiro[my][mx] is None:
            if self.vez % 2 == 0:
                self.tabuleiro[my][mx] = self.x.copy(mx, my)
            else:
                self.tabuleiro[my][mx] = self.circulo.copy(mx, my)
            
            self.vez += 1
        
            self.atualizar_jogo()
            self.tempo.marcar()
    
    def atualizar_jogo(self):
        # Atualiza estado do jogo (ocorrendo, empate, vitória)
        sequencias_bloqueadas = 0

        for possibilidade in POSSIBILIDADES_VITORIA:
            simbolo_x_contagem = 0
            simbolo_o_contagem = 0

            for i in range(3):
                x, y = possibilidade[i]
                simbolo = self.tabuleiro[y][x]

                if simbolo is not None:
                    if simbolo.simbolo == "X":
                        simbolo_x_contagem += 1
                    else:
                        simbolo_o_contagem += 1
            
            if simbolo_x_contagem == 3:
                self.vitoria(possibilidade)
                print("VITÓRIA DO X!")
                break
            elif simbolo_o_contagem == 3:
                self.vitoria(possibilidade)
                print("VITÓRIA DA BOLINHA!")
                break

            soma = simbolo_o_contagem + simbolo_x_contagem
            if soma == 2 or soma == 3:
                sequencias_bloqueadas += 1
        
        if sequencias_bloqueadas == 8:
            self.estado = EMPATE
            print("EMPATE!")
    
    def vitoria(self, possibilidade):
        self.estado = VITORIA
        self.possibilidade = possibilidade
    
    def reiniciar_jogo(self):
        self.estado = OCORRENDO
        self.possibilidade = None

        self.tabuleiro.clear()
        self.iniciar_tabuleiro()
    
    def desenhar_tabuleiro(self, janela):
        for i in range(2):
            pygame.draw.line(janela, BRANCO, (0, TAMANHO_CASA * (i + 1) - 5), (TAMANHO_CASA * 3, TAMANHO_CASA * (i + 1) - 5), 10)
        
        for i in range(2):
            pygame.draw.line(janela, BRANCO, (TAMANHO_CASA * (i + 1) - 5, 0), (TAMANHO_CASA * (i + 1) - 5, TAMANHO_CASA * 3), 10)
    
    def desenhar_simbolos(self, janela):
        for linha in self.tabuleiro:
            for simbolo in linha:
                if simbolo is not None:
                    simbolo.desenhar(janela)

    def desenhar_linha_vitoria(self, janela):
        # Vitória na diagonal 1
        if self.possibilidade == POSSIBILIDADES_VITORIA[6]:
            pos_inicial = self.possibilidade[0][0] * TAMANHO_CASA, self.possibilidade[0][1] * TAMANHO_CASA
            pos_final = (self.possibilidade[2][0] + 1) * TAMANHO_CASA, (self.possibilidade[2][1] + 1) * TAMANHO_CASA
            pygame.draw.line(
                janela,
                VERDE,
                pos_inicial, pos_final, 6
            )
        # Vitória na diagonal 2
        elif self.possibilidade == POSSIBILIDADES_VITORIA[7]:
            pos_inicial = (self.possibilidade[0][0] + 1) * TAMANHO_CASA, self.possibilidade[0][1] * TAMANHO_CASA
            pos_final = self.possibilidade[2][0] * TAMANHO_CASA, (self.possibilidade[2][1] + 1) * TAMANHO_CASA
            pygame.draw.line(
                janela,
                VERDE,
                pos_inicial, pos_final, 6
            )
        # Vitória na horizontal
        elif self.possibilidade == POSSIBILIDADES_VITORIA[0] or self.possibilidade == POSSIBILIDADES_VITORIA[1] or \
            self.possibilidade == POSSIBILIDADES_VITORIA[2]:

            pos_inicial = self.possibilidade[0][0] * TAMANHO_CASA, self.possibilidade[0][1] * TAMANHO_CASA + TAMANHO_CASA / 2
            pos_final = (self.possibilidade[2][0] + 1) * TAMANHO_CASA, self.possibilidade[2][1] * TAMANHO_CASA + TAMANHO_CASA / 2
            pygame.draw.line(
                janela,
                VERDE,
                pos_inicial, pos_final, 6
            )
        # Vitória na vertical
        else:
            pos_inicial = self.possibilidade[0][0] * TAMANHO_CASA + TAMANHO_CASA / 2, self.possibilidade[0][1] * TAMANHO_CASA
            pos_final = self.possibilidade[2][0] * TAMANHO_CASA + TAMANHO_CASA / 2, (self.possibilidade[2][1] + 1) * TAMANHO_CASA
            pygame.draw.line(
                janela,
                VERDE,
                pos_inicial, pos_final, 6
            )
    
    def desenhar_linha_empate(self, janela):
        pygame.draw.line(janela, AMARELO, (0, 0), (LARGURA, ALTURA), 6)
        pygame.draw.line(janela, AMARELO, (LARGURA, 0), (0, ALTURA), 6)

    def desenhar(self, janela):
        self.desenhar_tabuleiro(janela)
        self.desenhar_simbolos(janela)

        # Desenhar traço do simbolo (preview do simbolo)
        if self.tempo.acabar(0.10) and self.estado == OCORRENDO:
            if self.vez % 2 == 0:
                self.x.desenhar_traço(janela, self.ultima_mouse_pos[0], self.ultima_mouse_pos[1])
            else:
                self.circulo.desenhar_traço(janela, self.ultima_mouse_pos[0], self.ultima_mouse_pos[1])

        # Desenho para fim de jogo
        if self.estado == VITORIA:
            self.desenhar_linha_vitoria(janela)
        elif self.estado == EMPATE:
            self.desenhar_linha_empate(janela)
