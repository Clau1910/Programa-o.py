matriz = [
    [1,2,3],
    [4,5,6],
    [5,6,7]
]

elemento = matriz[0][1] = 777
print (elemento)

for linha in matriz:
    print(linha)

print ("\nPercorrendo a Matriz:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento na posição ({i}, {j}): {matriz[i][j]}")
