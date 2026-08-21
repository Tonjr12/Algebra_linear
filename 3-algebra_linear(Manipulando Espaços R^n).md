# Explicação: Trabalhando com Espaços Rn no NumPy

Este exercício demonstra como o Python lida com vetores de diferentes dimensões.

1. **Definição (`np.array`)**: Utilizamos o `np.array` para criar listas ordenadas de números reais. O NumPy trata esses dados como vetores matemáticos.
2. **Propriedade `.shape`**: O atributo `.shape` retorna a dimensão do array. Usamos `shape[0]` para identificar o número de elementos (a dimensão $n$ do espaço $R^n$).
3. **Validação**: Operações matemáticas (como a soma) só são possíveis entre vetores da mesma dimensão. O Python nos permite realizar essas operações respeitando a estrutura de tuplas ordenadas.