import Node as nd
import Block as bl


class Network:

    def __init__(self, index: int, name: str, nodes: [nd.Node]):
        self.index = index
        self.name = name
        self.nodes = nodes
        self.publicblocks: [bl.Block] = []

    def addNode(self, node: nd.Node):
        self.nodes.append(node)


