# 5
frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
numeros = [10, 25, 3, 47, 8, 15, 30]

print("--- Exercício 5: ---")
print(f"Sem negativos: Primeiro = {frutas[0]}, Último = {frutas[len(frutas)-1]}")
print(f"Com negativos: Primeiro = {frutas[0]}, Último = {frutas[-1]}\n")

print("--- Exercício 6 ---")
frutas.append('morango')      
frutas.insert(2, 'kiwi')      
print(f"Lista atualizada: {frutas}\n")

print("--- Exercício 7 ---")
frutas.remove('banana')       
print(f"Após remover 'banana': {frutas}\n")

print("--- Exercício 8: ---")
for n in numeros:
    if n > 15:
        print(n, end=" ")
print("\n")

print("--- Exercício 9: ---")
print(f"Crescente: {sorted(numeros)}")
print(f"Decrescente: {sorted(numeros, reverse=True)}")
print(f"Lista Original: {numeros}")   