dimensaoMatriz = int(input())

matriz = []
inicio = 1
for i in range(dimensaoMatriz):
    linha = []
    for j in range(inicio, dimensaoMatriz + inicio):
        linha.append(j)
    inicio = j + 1
    matriz.append(linha)

matrizVaziaParaDiagonalPrincipal = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append("   ")
    matrizVaziaParaDiagonalPrincipal.append(linha)

matrizDiagonalPrincipal = matrizVaziaParaDiagonalPrincipal
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matrizDiagonalPrincipal[i][j] = "  " + str(matriz[i][j])

matrizVaziaParaDiagonalSecundaria = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append("   ")
    matrizVaziaParaDiagonalSecundaria.append(linha)

matrizDiagonalSecundaria = matrizVaziaParaDiagonalSecundaria
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == len(matriz[i]) - (i + 1):
            matrizDiagonalSecundaria[i][j] = "  " + str(matriz[i][j])

print("Matriz:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j != (len(matriz[i]) -1):
            print("  " + str(matriz[i][j]), end = "")
        else:
            print("  " + str(matriz[i][j]))

print("")
print("Diagonal Principal:")
for i in range(len(matrizDiagonalPrincipal)):
    for j in range(len(matrizDiagonalPrincipal[i])):
        if j <= i:
            print(str(matrizDiagonalPrincipal[i][j]), end = "")
    print("")

print("")
print("Diagonal Secundaria:")
for i in range(len(matrizDiagonalSecundaria)):
    for j in range(len(matrizDiagonalSecundaria[i])):
        if j < dimensaoMatriz - i:
            print(str(matrizDiagonalSecundaria[i][j]), end="")
    print("")
