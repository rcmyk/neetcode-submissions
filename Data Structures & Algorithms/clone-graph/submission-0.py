"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:

    def __init__(self):
        self.nodeCache = {}

    def cloneNode(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        if node in self.nodeCache:
            return self.nodeCache[node]

        new_node = Node(node.val, [])
        self.nodeCache[node] = new_node

        for n in node.neighbors:
            new_node.neighbors.append(self.cloneNode(n))

        return new_node
        

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        return self.cloneNode(node)
