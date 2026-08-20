import numpy as np  # Importa a biblioteca NumPy para manipulação de arrays e vetores

# 1. Definição do Vetor:
# Criamos um vetor em 3 dimensões (3D) usando np.array.
# No NumPy, o array atua como a estrutura de dados ideal para representar componentes vetoriais.
vetor_a = np.array([3, 4, 5])

# 2. Multiplicação por Escalar:
# Ao multiplicar um vetor por um número escalar (neste caso, o número 2),
# o NumPy aplica a multiplicação individualmente a cada um dos seus elementos (3*2, 4*2, 5*2).
vetor_dobrado = vetor_a * 2

# 3. Exibição dos Resultados:
print("Vetor original:", vetor_a)
print("Vetor dobrado (multiplicado por 2):", vetor_dobrado)