import numpy as np  # Importa a biblioteca NumPy e a apelida como 'np' para facilitar o uso

# Criando vetores usando np.array.
# O array do NumPy é otimizado para operações matemáticas vetoriais.
vetor_a = np.array([3, 4, 5])
vetor_b = np.array([6, 7, 8])

# Multiplicação por escalar:
# O NumPy aplica a operação em cada elemento do vetor individualmente.
vetor_dobrado = vetor_a * 2

# Adição de vetores:
# Realiza a soma componente a componente (Ex: 3+6, 4+7, 5+8).
soma = vetor_a + vetor_b

# Exibindo os resultados no console:
print("Vetor A original:", vetor_a)
print("Vetor A dobrado (multiplicado por 2):", vetor_dobrado)
# Usamos f-string (f"...") para formatar o texto e exibir as variáveis de forma legível
print(f"Soma dos vetores {vetor_a} + {vetor_b}:", soma)