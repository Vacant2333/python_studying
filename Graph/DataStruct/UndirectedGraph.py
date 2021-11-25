class UndirectedGraph:
    # Node [str]
    nodes = []
    # Edge [[node_1, node_2]]
    edges = []

    def get_nodes(self) -> list:
        return self.nodes

    def get_node_neighbor(self, node: str) -> list:
        neighbor = []
        for edge in self.edges:
            if node in edge:
                neighbor.append(edge[1] if edge.index(node) == 0 else edge[0])
        return neighbor

    def get_edges(self) -> list:
        return self.edges

    def add_node(self, node: str or list):
        if isinstance(node, str):
            # Node type is str
            self.check_node(node)
            self.nodes.append(node)
        elif isinstance(node, list):
            # Node type is list(multiple node)
            for one_node in node:
                self.check_node(one_node)
                self.nodes.append(one_node)
        else:
            # Node type is not str or list
            raise ValueError("Node must be str or list[str]! node:" + str(node))

    def add_edge(self, edge: list):
        if isinstance(edge, list):
            if isinstance(edge[0], list):
                # Multiple edge
                for one_edge in edge:
                    self.check_edge(one_edge)
                    self.edges.append(one_edge)
            else:
                # Single edge
                self.check_edge(edge)
                self.edges.append(edge)
        else:
            raise ValueError("Edge must be list! edge:" + str(edge))

    def check_node(self, node: str, check_repeat=True):
        # Check type
        if not isinstance(node, str):
            raise ValueError("Node must be str! node:" + str(node))
        # Check length
        if len(node) == 0:
            raise ValueError("Node length must > 0! node:" + node)
        # Check repeat
        if check_repeat and node in self.nodes:
            raise ValueError("Node duplication! node:" + node)

    def check_edge(self, edge: list):
        # Check type
        if not isinstance(edge, list):
            raise ValueError("Edge must be list! edge:" + str(edge))
        # Check length
        if len(edge) != 2:
            raise ValueError("Edge length must be 2" + str(edge))
        # Check Node Value
        self.check_node(edge[0], False)
        self.check_node(edge[1], False)
        # Check node if in nodes
        if edge[0] not in self.nodes or edge[1] not in self.nodes:
            raise ValueError("Edge node error! node:" + str(edge))
        # Check edge if duplication
        if edge in self.edges or edge[::-1] in self.edges:
            raise ValueError("Edge duplication! edge" + str(edge))
