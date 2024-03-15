import numpy as np
import time


# Definir o tamanho da sequencia
n = 10*4
# Definir o número de buscas
q = 10**2

# Gerar uma sequencia com inteiros aleatorios entre 0 e n
sequencia = np.random.randint(0, n, n)

# Gerar uma matriz com q valores para serem buscados
buscas = np.random.randint(0, q , q)

inicio_do_programa = time.time()

# Ordenar a sequencia
sequencia_ordenada = np.sort(sequencia, kind='mergesort')

# Função para busca sequencial otimizada
def busca_sequencial_otimizada(sequencia_ordenada, chave):
    for i, valor in enumerate(sequencia_ordenada):
        if valor == chave:
            return i  # Retorna a posição se a chave for encontrada
        elif valor > chave:
            return -1  # Chave não está na sequência se o valor for maior que a chave
    return -1  # Retorna -1 se a chave não for encontrada

for chave in buscas:
    posicao = busca_sequencial_otimizada(sequencia_ordenada, chave)

fim_do_programa = time.time()
tempo_total = fim_do_programa - inicio_do_programa
print(f"Tempo total: {tempo_total:.6f} segundos.")
