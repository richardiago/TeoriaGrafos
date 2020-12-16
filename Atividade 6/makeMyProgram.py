'''
Nome: Iago Richard da Anunciação da Silva
RA: 21038514

Atividade 6 - Teoria dos Grafos

Descrição: Aplica busca em profundidade para gerar a ordenação topologica de compilações
Entrada: makefile
Saida: instruções de execução para compilação do alvo definido no makefile
'''
#Variaveis globais
dependencias = dict() # dicionário que armazena as dependências de cada vértice
instrucoes   = dict() # dicionário que armazena as instruções de cada vértice
vertices     = dict() # dicionário que relaciona cada vértice a um numero ex: ['graph.o' : 1]
adjacencias  = []     # lista de adjacências
vis          = []     # vetor de visitados
pos          = []     # lista que armazena a ordenação topológica

#Relaciona cada vértice a um número inteiro
def relacionaVertices():

    i = 0
    for k, v in dependencias.items():
        vertices[k] = i
        i += 1

#Constroi lista de adjacências
def constroiListas():

    for k, v in dependencias.items():
        adjacencias.append([])

        for i in v:
            if i in vertices:
                adjacencias[vertices[k]].append(vertices[i])

# Busca em Profundidade
def dfs(alvo):
    for i in range(len(adjacencias)):
        vis.append(False)

    # Vai rodar no alvo e nas dependencias do alvo
    x = [vertices[alvo]]
    y = x + adjacencias[vertices[alvo]]
    for j in y:
        if vis[j] == False:
            dfs_search(j)

def dfs_search(u):
    vis[u]   = True

    for i in adjacencias[u]:
        if vis[i] == False:
            dfs_search(i)

    pos.append(u)
    
def main():

    linha = ''
    alvo  = ''
    vert  = ''

    #Recebe a entrada
    while (linha != 'FIM'):

        linha = input()

        if (linha.split()[0] == 'make'):
            alvo = linha.split()[1]
        
        elif(linha[0] != '\t' and linha.split()[0] != 'FIM'):
            vert = (linha.split()[0]).replace(':', '')
            dep = (linha.split())[1:]
            dependencias[vert] = dep

        elif(linha[0] == '\t'):
            
            if(vert in instrucoes):
                instrucoes[vert] = instrucoes[vert] + '\n' + linha.lstrip()
            else:
                instrucoes[vert] = linha.lstrip()

    relacionaVertices()
    constroiListas()
    dfs(alvo)

    key_list = list(vertices.keys())
    val_list = list(vertices.values())

    for i in pos:
        v = key_list[val_list.index(i)]
        print(instrucoes[v])

main()    