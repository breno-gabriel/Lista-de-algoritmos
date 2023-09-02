class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicionar_arestas(self, v1, v2):
        self.grafo[v1].insert(0, v2)
        self.grafo[v2].insert(0, v1)

    def lista_vazia(self, lista):
        if len(lista) == 0:
            return True
        else:
            return False

    def imprimir_listas(self):
        for i in range(self.vertices):
            print("{}: ".format(i), end="")
            if not self.lista_vazia(self.grafo[i]):
                for j in self.grafo[i]:
                    print("{} ".format(j), end="")
            else:
                print("Lista Vazia", end="")
            print("")

    def buscaProfundidade(self):
        marcado = [False] * self.vertices
        percurso = [0]
        self.dfs(0, marcado, percurso)
        return percurso

    def dfs(self, v, marcado, percurso):
        marcado[v] = True
        for vizinho in self.grafo[v]:
            if not marcado[vizinho]:
                percurso.append(vizinho)
                self.dfs(vizinho, marcado, percurso)


def main():
    num_vertices = int(input())
    grafo = Grafo(num_vertices)

    Flag = True
    while Flag:
        aresta = input()
        params = aresta.split(" ")
        for i in range(len(params)):
            params[i] = int(params[i])
        grafo.adicionar_arestas(params[0], params[1])
        if params[2] == 0:
            Flag = False

    grafo.imprimir_listas()
    print("")
    percurso = grafo.buscaProfundidade()
    caminho = ""
    for i in percurso:
        caminho += str(i)
        caminho += " "
    print(caminho, end="")


if __name__ == '__main__':
    main()