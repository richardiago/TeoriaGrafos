'''
Nome: Iago Richard da Anunciação da Silva
RA: 21038514

Atividade 2 - Teoria dos Grafos

Esse programa tem como objetivo principal verificar se uma certa configuração de churrasco é épica ou não.
Para tal temos os seguintes sub-objetivos:
- Receber os dados 
- Montar uma matriz de adjacencia
- Montar uma lista de listas de convidados 
- Para cada lista verificar se os convidados da mesma se conhecem a partir da matriz de adjacencia
- Retornar o resultado.

ENTRADA: quantidade de vértices, quantidade de arestas, arestas, quantidade de configurações diferentes de convidados,
listas de convidados

SAIDA: SIM caso o churrasco seja épico, ou NAO caso não seja.
'''

# Devolve uma matriz de adjacencia de ordem |v|, zerada
def constroiMatriz(v):

    matriz = []

    for i in range(v):
        matriz.append([])

        for j in range(v):
            matriz[i].append([])
            matriz[i][j] = 0

    return matriz

# Insere uma aresta ligando os vertices u e v na matriz e retorna-a
def insereAresta(matriz, u, v):

    matriz[u][v] = 1
    matriz[v][u] = 1

    return matriz

# Imprime uma matriz
def imprimeMatriz(matriz):

    for i in range(len(matriz)):
        print(matriz[i])

# Verifica se todos os vertices em conf são vizinhos na matriz
def verificaConfiguracao(matriz, conf):

    for j in range(len(conf)):
        for k in range(j+1, len(conf)):
            if(matriz[conf[j]][conf[k]] == 0):
                return 'NAO'

    return 'SIM'

# Função principal
def main():

    v = int(input()) #quantidade de vertices
    e = int(input()) #quantidade de arestas

    matriz = constroiMatriz(v)

    # Recebe as arestas
    for i in range(e):
        aresta = input().split()
        x, y = int(aresta[0]), int(aresta[1])
        matriz = insereAresta(matriz, x, y)

    n = int(input()) #quantidade de configurações

    conf = []

    # Recebe as configuracoes
    for i in range(n):
        c = input().split()
        c = list(map(int, c))
        del c[0]
        conf.append(c)

    resultados = []

    # Verifica os resultados e armazena no vetor resultados
    for i in range(len(conf)):
        resultados.append(verificaConfiguracao(matriz, conf[i]))

    # Imprime todos os resultados
    imprimeMatriz(resultados)

main()

