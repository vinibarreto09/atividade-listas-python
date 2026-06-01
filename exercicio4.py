notas = [7.5, 8.0, 6.0, 9.5, 5.5, 8.5, 7.0, 9.0, 6.5, 8.0]
nomes = ['Carlos', 'Ana', 'Bruno', 'Ana', 'Diego', 'Ana', 'Bruno']

# 1
soma_notas = sum(notas)
quantidade_notas = len(notas)
media = soma_notas / quantidade_notas

print(f"1. Média da turma: {media:.2f}")

# 2
maior_nota = max(notas)
menor_nota = min(notas)

alunos_acima_media = 0
for nota in notas:
    if nota > media:
        alunos_acima_media += 1

print(f"2. Maior nota: {maior_nota} | Menor nota: {menor_nota}")
print(f"   Alunos acima da média: {alunos_acima_media}")

# 3
contagem_ana = nomes.count('Ana')
print(f"3. Ocorrências de 'Ana': {contagem_ana}")

# 4
indice_bruno = nomes.index('Bruno')
print(f"4. Índice da primeira ocorrência de 'Bruno': {indice_bruno}")

# 5
nomes_unicos = []
for nome in nomes:
    if nome not in nomes_unicos:
        nomes_unicos.append(nome)

print(f"5. Lista sem repetições: {nomes_unicos}")   