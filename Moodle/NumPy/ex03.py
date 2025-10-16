import numpy as np

matriz = np.zeros((2, 2), dtype=int)

linha_bomba, coluna_bomba = map(int, input().split())

matriz[linha_bomba][coluna_bomba] = 1

bomba_encontrada = False

for _ in range(3):

    linha_jogada, coluna_jogada = map(int, input().split())

    if matriz[linha_jogada][coluna_jogada] == 1:

        bomba_encontrada = True

if bomba_encontrada:

    print("Game Over! Try Again!")
else:

    print("Congratulations! You beat the game!")