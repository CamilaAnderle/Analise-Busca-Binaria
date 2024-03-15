import numpy as np
import time


# Definir o tamanho da sequencia
n = 10**7
# Definir o numero de buscas
q = 10**5

# Gerar uma sequencia com inteiros aleatorios entre 0 e n
sequencia = np.random.randint(0, n, n)

# Gerar uma matriz com q valores para serem buscados
buscas = np.random.randint(0, q , q)

# Função para busca sequencial
def busca_sequencial(sequencia, chave):
    for i, valor in enumerate(sequencia):
        if valor == chave:
            return i  # Retorna a posição se a chave for encontrada
    return -1  # Retorna -1 se a chave não for encontrada


inicio_do_programa = time.time()


for chave in buscas:
    posicao = busca_sequencial(sequencia, chave)


fim_do_programa = time.time()

tempo_total = fim_do_programa - inicio_do_programa

print(f"Tempo total: {tempo_total:.6f} segundos.")

