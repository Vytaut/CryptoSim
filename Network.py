import Node as nd


class Network:

    def __init__(self, index: int, name: str, nodes: [nd.Node]):
        self.index = index
        self.name = name
        self.nodes = nodes
