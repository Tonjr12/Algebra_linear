import numpy as np

# Definindo um vetor no espaço R2 (duas dimensões)
r2_vetor = np.array([3, 4])

# Definindo um vetor no espaço R3 (três dimensões)
r3_vetor = np.array([-1, 5, 3])

# Verificando a dimensão (tamanho da tupla)
print(f"Dimensão do r2_vetor: {r2_vetor.shape[0]} (pertence ao R2)")
print(f"Dimensão do r3_vetor: {r3_vetor.shape[0]} (pertence ao R3)")

# Operação de soma em R3
vetor_soma = r3_vetor + np.array([1, 1, 1])
print(f"Resultado da soma no R3: {vetor_soma}")