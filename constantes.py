# Janela
ALTURA = LARGURA = 600
TAMANHO_CASA = ALTURA // 3
FPS = 60

# Tabuleiro
LINHAS = COLUNAS = 3
POSSIBILIDADES_VITORIA = (
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2))
)

# Estados do jogo
OCORRENDO = 0
EMPATE = 1
VITORIA = 2

# Cores
BRANCO = 255, 255, 255,
PRETO = 0, 0, 0,
CINZA = 128, 128, 128,
VERMELHO = 255, 0, 0
VERDE = 0, 255, 0,
AMARELO = 255, 255, 0

# Simbolos
SIMBOLO_O = "O"
SIMBOLO_X = "X"
