'''
Nome: Iago Richard da Anunciação da Silva
RA: 21038514

Atividade 3 - Teoria dos Grafos

Descrição: conta a quantidade n de componentes conexas de um grafo e devolve n-1, que é o numero minimo de arestas para conectar todo o grafo
Entrada: quantidade de vértices, quantidade de arestas, e as arestas
Saida: # de novos voos: n-1, sendo n a quantidade de componentes conexas do grafo
'''

# retorna uma matriz de listas de adjacencias de ordem |v|
def constroiListas(v):

    adjacencias = []

    for i in range(v):
        adjacencias.append([])

    return adjacencias

# adiciona aresta entre os vétices x e y, em ambas as listas de adjacencia
def adicionaLista(adjacencias, x, y):
    
    adjacencias[x].append(y)
    adjacencias[y].append(x)

    return adjacencias

# Retorna o primeiro vertice que ainda não foi visitado, caso todos tenham sido visitados retorna False
def verificaVisitados(vis):

    for i in range(len(vis)):
        if vis[i] == False:
            return i

    return False

# Roda a busca BFS a primeira vez, e depois roda mais uma vez pra cada componente conexa
def chamaBFS(adjacencias, raiz):

    vis  = [] # vetor de visitados
    n    = 1  # quant. de componentes conexas

    for i in range(len(adjacencias)):
        vis.append(False)

    vis = bfs(adjacencias, raiz, vis)

    while verificaVisitados(vis) != False:
        vis = bfs(adjacencias, verificaVisitados(vis), vis)
        n +=1

    return n

# busca BFS, retorna o vetor de visitados
def bfs(adjacencias, raiz, vis):

    fila = [] # fila de 'visitação'

    vis[raiz] = True
    fila.append(raiz)

    while len(fila) > 0:
        u = fila.pop(0)

        for j in adjacencias[u]:
            if vis[j] == False:
                vis[j]  = True
                fila.append(j)

    return vis

# Imprime uma matriz
def imprimeMatriz(matriz):

    for i in range(len(matriz)):
        print(matriz[i])


def main():

    v = int(input()) #quantidade de vertices
    e = int(input()) #quantidade de arestas

    adjacencias = constroiListas(v)

    # Recebe as arestas
    for i in range(e):
        aresta = input().split()
        x, y = int(aresta[0]), int(aresta[1])
        adjacencias = adicionaLista(adjacencias, x, y)

    # Busca em largura
    n = chamaBFS(adjacencias, 0)

    print('# de novos voos: ', n-1)

main()