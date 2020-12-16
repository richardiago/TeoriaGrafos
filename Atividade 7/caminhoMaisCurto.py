'''
Nome: Iago Richard da Anunciação da Silva
RA: 21038514

Atividade 7 - Teoria dos Grafos

Descrição: Executa o algoritmo de Dijkstra com fila de prioridades implementada como heap
Entrada: Quantidade de vértices, quantidade de arcos, arcos, vértice de origem e vértice de destino
Saida: Tamanho do caminho minimo a partir da origem até o destino
'''

#Variaveis globais
adjacencias  = []     # lista de adjacências
cost         = []     # vetor de custos
pred         = []     # vetor de predecessores
heap         = []     # fila de prioridades (heap)

# Funções de Heap
def pai(i):
    return i // 2

def filho_esquerdo(i):
    return 2*i

def filho_direito(i):
    return 2*i + 1

#Insere na heap
def heap_insert(v, val):

    heap.append([v, val])
    corrige_subindo(len(heap) - 1)

def corrige_subindo(i):
    
    while (i > 1 and heap[pai(i)][1] > heap[i][1]):

        heap[pai(i)], heap[i] = heap[i], heap[pai(i)]
        i = pai(i)
        
#Extrai o topo da árvore
def extract_min():

    min = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    corrige_descendo(1)

    return min

def corrige_descendo(i):

    e = filho_esquerdo(i)
    d = filho_direito(i)

    if (e <= len(heap)-1 and heap[e][1] < heap[i][1]):
        menor = e
    
    else:
        menor = i
    
    if (d <= len(heap)-1 and heap[d][1] < heap[menor][1]):
        menor = d

    if (menor != i):
        heap[i], heap[menor] = heap[menor], heap[i]
        corrige_descendo(menor)

#Muda a prioridade de um vértice na heap
def change(vertice, prioridade):

    v = None

    for j in range(1, len(heap)):
        if (heap[j][0] == vertice):
            v = j
            break

    if v == None:
        return
        
    heap[v][1] = prioridade
    corrige_subindo(v)

#Algoritmo de Dijkstra
def Dijkstra(origem):

    cost[origem] = 0.0
    pred[origem] = origem
    
    change(origem, 0.0)
    
    while(len(heap) > 1):
        
        u = extract_min()

        if(u[1] == float('inf')):
            return

        for i in range(len(adjacencias[u[0]])):
            k = adjacencias[u[0]][i]
            relax(u[0], k[0], k[1])

#Faz a relaxação dos arcos
def relax(u, v, weight):
    
    if(cost[v] > cost[u] + weight):
        cost[v] = cost[u] + weight
        pred[v] = u
        change(v, cost[v])

# Inicializa as listas globais
def constroiListas(v):

    heap.append([])

    for i in range(v):
        adjacencias.append([])
        cost.append(float('inf'))
        pred.append(None)
        heap_insert(i, float('inf'))
        
# Imprime uma matriz
def imprimeMatriz(matriz):

    for i in range(len(matriz)):
        print(matriz[i])

def main():

    v = int(input()) #quantidade de vertices
    e = int(input()) #quantidade de arestas

    constroiListas(v)

    for i in range(e):
        valores = input().split()
        o = int(valores[0])
        d = int(valores[1])
        dist = float(valores[2])

        adjacencias[o].append([d, dist])

    aux = input().split()
    origem, destino = int(aux[0]), int(aux[1])

    Dijkstra(origem)

    if(cost[destino] == float('inf')):
        print('ERRO: 3.1415')
    else:
        print('%.4f' %(round(cost[destino], 4)))

main()   