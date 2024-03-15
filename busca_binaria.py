import numpy as np
import time
#import matplotlib.pyplot as plt

# Definir o tamanho da sequencia
n = 10**4
# Definir o número de buscas
q = 10**2

# Gerar uma sequencia com inteiros aleatorios entre 0 e n
sequencia = np.random.randint(0, n , n)

# Gerar uma matriz com q valores para serem buscados
buscas = np.random.randint(0, q , q)

inicio_do_programa = time.time()

# Ordenar a sequencia
sequencia_ordenada = np.sort(sequencia, kind ='mergesort')

# Realizar busca binária para cada chave na matriz buscas
tempos_de_busca = []

for chave in buscas:
    posicao = np.searchsorted(sequencia_ordenada, chave)


fim_do_programa = time.time()
tempo_total = fim_do_programa - inicio_do_programa
print(f"Tempo total: {tempo_total:.6f} segundos.")



