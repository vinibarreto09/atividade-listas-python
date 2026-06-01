palavras = ['python', 'lista', 'programação', 'código', 'loop', 'função']
numeros = list(range(1, 21))  

# 1
quadrados_1_a_10 = [x**2 for x in range(1, 11)]
print(f"1. Quadrados de 1 a 10: {quadrados_1_a_10}")

# 2
pares = [x for x in numeros if x % 2 == 0]
print(f"2. Números pares: {pares}")

# 3
comprimentos = [len(palavra) for palavra in palavras]
print(f"3. Comprimentos das palavras: {comprimentos}")

# 4
palavras_longas_maiusculas = [palavra.upper() for palavra in palavras if len(palavra) > 5]
print(f"4. Palavras longas em maiúsculas: {palavras_longas_maiusculas}")

# 5
tuplas_quadrados = [(x, x**2) for x in range(1, 6)]
print(f"5. Tuplas (número, quadrado): {tuplas_quadrados}")
