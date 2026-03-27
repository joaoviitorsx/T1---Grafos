class Graph:
    def __init__(self, vertices):
        self._v = vertices
        self._e = 0
        self._adj = [[] for _ in range(vertices)]

    @classmethod
    def from_file(cls, path):
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        vertices = int(lines[0])
        edges = int(lines[1])
        graph = cls(vertices)

        for line in lines[2:]:
            v, w = map(int, line.split())
            graph.add_edge(v, w)

        if graph.e() != edges:
            raise ValueError(
                f"Quantidade de arestas inconsistente: esperado {edges}, obtido {graph.e()}"
            )

        return graph

    def add_edge(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._adj[v].sort()
        self._adj[w].sort()
        self._e += 1

    def adj(self, v):
        self._validate_vertex(v)
        return self._adj[v]

    def v(self):
        return self._v

    def e(self):
        return self._e

    def _validate_vertex(self, v):
        if v < 0 or v >= self._v:
            raise ValueError(f"Vértice inválido: {v}")