class DepthFirstPaths:
    def __init__(self, graph, source):
        self._source = source
        self._marked = [False] * graph.v()
        self._edge_to = [None] * graph.v()
        self._visit_order = []
        self._dfs(graph, source)

    def _dfs(self, graph, v):
        self._marked[v] = True
        self._visit_order.append(v)

        for w in graph.adj(v):
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(graph, w)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = []
        current = v
        while current != self._source:
            path.append(current)
            current = self._edge_to[current]
        path.append(self._source)
        path.reverse()
        return path

    def reachable_vertices(self):
        return [v for v, marked in enumerate(self._marked) if marked]

    def visit_order(self):
        return self._visit_order[:]