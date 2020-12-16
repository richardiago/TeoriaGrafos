'''
Nome: Iago Richard da Anunciação da Silva
RA: 21038514

Atividade 5 - Teoria dos Grafos

Descrição: Aplica o algoritmo de Kruskal usando estrutura Union Find
Entrada: Quantidade n de coordenadas, e n coordenadas
Saida: comprimento de cabeamento minimo: N, seguido das ligações entre as Ystations

'''
#Biblioteca para usar a função de raiz quadrada
import math

# Vetores globais
leader     = []
size       = []
distancias = []
H          = []

# Métodos da estrutura Union-Find
def set_init(n):

    for i in range(n):
        leader.append(i)
        size.append(i)

def find_set(x):

    i = leader[x]

    while leader[i] != i:
        i = leader[i]
    
    return leader[i]

def union(x, y):

    lx = find_set(x)
    ly = find_set(y)

    if size[lx] <= size[ly]:
        leader[lx] = ly
        size[ly] += size[lx]

    else:
        leader[ly] = lx
        size[lx] += size[ly]


# Algoritmo de Kruskal
def Kruskal(n):

    F = sorted(distancias, key = lambda x: x[2])
    set_init(n)

    for i in range(len(F)):
        aresta = F[i]

        if find_set(aresta[0]) != find_set(aresta[1]):
            union(aresta[0], aresta[1])
            H.append(aresta)
            
# Dada as coordenadas calcula a distância entre dois pontos
def calculaDistancia(Xa, Ya, Xb, Yb):

    return math.sqrt((Xb - Xa) ** 2 + (Yb - Ya) ** 2)

# Monta uma matriz com as distancias entre cadas par de pontos
def montaMatrizDistancias(coordenadas):

    for i in range(len(coordenadas)):
        for j in range(i+1, len(coordenadas)):
            distancias.append([i, j, calculaDistancia(coordenadas[i][0], coordenadas[i][1], coordenadas[j][0], coordenadas[j][1])])


# Imprime uma matriz
def imprimeMatriz(matriz):

    for i in range(len(matriz)):
        print(matriz[i])


def main():

    v = int(input()) #quantidade de coordenadas

    coordenadas = []

    # Recebe as coordenadas
    for i in range(v):
        coord = input().split()
        x, y = int(coord[0]), int(coord[1])
        coordenadas.append([x,y])

    montaMatrizDistancias(coordenadas)
    Kruskal(v)

    G = sorted(H, key = lambda x: (x[0], x[1]))

    soma = 0
    for i in range(len(G)):
        soma += G[i][2]

    print('comprimento de cabeamento minimo: %.4f' %(round(soma, 4)))

    for i in range(len(G)):
        print(G[i][0], G[i][1])

main()



