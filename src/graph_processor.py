from collections import defaultdict
import random

from graph import Grafo


class GraphProcessor:
    """
    Classe de manipulação de grafos
    """

    def __init__(self, input_format, input_content):
        self.input_format = input_format
        self.input_content = input_content
        self.adj = defaultdict(set)
        if input_content is not None:
            self.grafo = Grafo(input_content)
        else:
            self.grafo = None

        self.grafo.print_grafo()

    def criacao_grafo_x_vertices(self, extra_args):
        print(f"Execuntando 'criacao_grafo_x_vertices' [extra_args={extra_args}]")

        # Gerando um grafo com x vértices aleatóriamente com letras de A a Z não repetidas
        vertices = []
        for i in range(0, int(extra_args)):
            random_number = random.randint(1, 11000)
            if random_number not in vertices:
                vertices.append(random_number)
            else:
                random_number = random.randint(1, 11000)
                vertices.append(random_number)

        print("Vertices: ", vertices)

        # Víncula os vertices ao primeiro vertice
        arestas = []
        for i in range(1, len(vertices)):
            arestas.append((vertices[0], vertices[i]))

        # Cria e imprime o grafo.
        self.grafo = Grafo(arestas, direcionado=True)
        print(self.grafo)

    def criacao_arestas(self, extra_args):
        print(f"Execuntando 'criacao_arestas' [extra_args={extra_args}]")

        # gera arestas aleatórias a classe Grafo sem criar arestas repetidas
        arestas = self.grafo.get_arestas()
        novas_arestas = []
        for i in range(0, int(extra_args)):
            random_number = random.randint(1, 11000)
            if random_number not in arestas:
                novas_arestas.append([i, random_number])
            else:
                random_number = random.randint(1, 11000)
                novas_arestas.append([i, random_number])

        print("Arestas Originais: ", arestas)
        print("Arestas Novas: ", novas_arestas)

        self.grafo.adiciona_arestas(novas_arestas)

    def remocao_arestas(self, extra_args):
        print(f"Execuntando 'remocao_arestas' [extra_args={extra_args}]")

        extra_args = extra_args.split("|")
        print(extra_args)

        for extra_arg in extra_args:
            aux = extra_arg.split(";")
            self.grafo.remove_arco(aux[0], aux[1])

    def rotulacao_vertices(self):
        print(f"Execuntando 'rotulacao_vertices'")
        self.grafo.rotula_vertices()

    def busca_em_profundidade(self, extra_args):
        print(f"Execuntando 'busca_em_profundidade' [extra_args={extra_args}]")
        self.grafo.busca_em_profundidade(extra_args)

    def busca_em_largura(self, extra_args):
        print(f"Execuntando 'busca_em_largura' [extra_args={extra_args}]")
        self.grafo.busca_em_largura(extra_args)

    def componentes_conexas(self):
        print(f"Execuntando 'componentes_conexas'")
        self.grafo.componentes_conexas()

    def caminho_minimo(self, extra_args):
        print(f"Execuntando 'caminho_minimo' [extra_args={extra_args}]")
        self.grafo.caminho_minimo(extra_args)

    def ponderacao_arestas(self, extra_args):
        print(f"Execuntando 'ponderacao_arestas' [extra_args={extra_args}]")
        # TODO: Implementar
        self.grafo.pondera_arestas()

    def rotulacao_vertices(self, extra_args):
        print(f"Execuntando 'rotulacao_vertices' [extra_args={extra_args}]")
        self.grafo.rotula_vertices(extra_args)

    def rotulacao_arestas(self, extra_args):
        print(f"Execuntando 'rotulacao_arestas' [extra_args={extra_args}]")
        self.grafo.rotula_arestas(extra_args)

    def checagem_adjacencia_vertices(self, extra_args):
        print(f"Execuntando 'checagem_adjacencia_vertices' [extra_args={extra_args}]")

        adjacentes = self.grafo.vertices_adjacentes(extra_args)

        print(f"Adjacentes ao vertice {extra_args}: ", adjacentes)

    def checagem_adjacencia_arestas(self, extra_args):
        print(f"Execuntando 'checagem_adjacencia_arestas' [extra_args={extra_args}]")

        adjacentes = self.grafo.arestas_adjacentes(extra_args)

        print(f"Adjacentes a aresta {extra_args}: ", adjacentes)

    def checagem_existencia_arestas(self, extra_args):
        print(f"Execuntando 'checagem_existencia_arestas' [extra_args={extra_args}]")

        extra_args = extra_args.split(";")

        arestas = self.grafo.existe_aresta(extra_args[0], extra_args[1])

        print(f"Existe aresta entre {extra_args[0]} e {extra_args[1]}? {arestas}")

    def checagem_quantidade_vertices(self):
        print(f"Execuntando 'checagem_quantidade_vertices'")

        print(f"Quantidade de vertices: {len(self.grafo.get_vertices())}")

    def checagem_quantidade_arestas(self):
        print(f"Execuntando 'checagem_quantidade_arestas'")

        print(f"Quantidade de arestas: {len(self.grafo.get_arestas())}")

    def checagem_grafo_vazio(self):
        print(f"Execuntando 'checagem_grafo_vazio'")

        if not self.grafo.get_arestas():
            print("Grafo vazio")
        else:
            print("Grafo não vazio")

    def checagem_grafo_completo(self):
        print(f"Execuntando 'checagem_grafo_completo'")

        if self.grafo.grafo_completo():
            print("Grafo completo")
        else:
            print("Grafo não completo")
