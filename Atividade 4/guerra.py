'''
Nome: Iago Richard da Anunciação da Silva
RA: 21038514

Atividade 4 - Teoria dos Grafos

Descrição: Identifica quais são os vértices de corte do grafo através de uma busca em profundidade
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

# inicializa os vetores de visitados, predecessor, ordem e low e chama dfs_search pra cada componente do grafo
def dfs(raiz, v, adjacencias):

    vis   = []
    pred  = []
    corte = []
    ordem   = []
    low   = []

    for i in range(v):
        vis.append(False)
        pred.append(None)
        ordem.append(0)
        low.append(0)

    count = 0
    vis, corte, count, ordem, low, pred = dfs_search(raiz, vis, corte, count, ordem, low, adjacencias, pred)

    while verificaVisitados(vis) != False:
        vis, corte, count, ordem, low, pred = dfs_search(verificaVisitados(vis), vis, corte, count, ordem, low, adjacencias, pred)

    return corte

# executa busca em profundidade e preenche o vetor 'corte' com os vértices de corte do grafo
def dfs_search(u, vis, corte, count, ordem, low, adjacencias, pred):
    
    vis[u]   = True
    count   += 1
    ordem[u] = count
    low[u]   = count
    n_filhos = 0


    for i in adjacencias[u]:
        if vis[i] == False:
            
            pred[i] = u
            n_filhos += 1
            vis, corte, count, ordem, low, pred = dfs_search(i, vis, corte, count, ordem, low, adjacencias, pred)

            if pred[u] == None and n_filhos > 1:
                corte.append(u)

            if pred[u] != None and low[i] >= ordem[u]:
                corte.append(u)

            low[u] = min(low[u], low[i])

        else:
            if i != pred[i]:
                low[u] = min(low[u], ordem[i])

    return vis, corte, count, ordem, low, pred

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


    corte = dfs(0, v, adjacencias)
    corte = sorted(set(corte))

    print('# de alvos possiveis: ', len(corte))
    imprimeMatriz(corte)

main()