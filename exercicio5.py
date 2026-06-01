turma = [
    ['Alice', 8.0, 7.5, 9.0],
    ['Bruno', 6.5, 7.0, 8.0],
    ['Carla', 9.5, 9.0, 9.5],
    ['Diego', 5.0, 6.0, 5.5],
    ['Elena', 7.0, 8.5, 7.5],
]
resultados = []

# 1
print("### Médias Individuais ###")
for aluno in turma:
    nome = aluno[0]
    notas = aluno[1:] 
    media = sum(notas) / len(notas)
    resultados.append([nome, media])
    print(f"{nome}: {media:.2f}")

# 2
melhor_aluno = max(resultados, key=lambda x: x[1])
print(f"\n### Maior Média ###")
print(f"Aluno: {melhor_aluno[0]} | Média: {melhor_aluno[1]:.2f}")

# 3
aprovados = [r[0] for r in resultados if r[1] >= 6.0]
reprovados = [r[0] for r in resultados if r[1] < 6.0]

print(f"\n### Situação dos Alunos ###")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

# 4
soma_medias = sum(r[1] for r in resultados)
media_geral = soma_medias / len(resultados)
print(f"\n### Média Geral da Turma ###")
print(f"{media_geral:.2f}")

# 5
novo_aluno = ['Felipe', 8.0, 7.5, 8.5]
turma.append(novo_aluno)

resultados = []
for aluno in turma:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / len(notas)
    resultados.append([nome, media])

ranking = sorted(resultados, key=lambda x: x[1], reverse=True)

print(f"\n Ranking Final (Decrescente) ")
for pos, item in enumerate(ranking, 1):
    print(f"{pos}. {item[0]} - Média: {item[1]:.2f}")   