class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # +1 because 1 based indexing,
        # but the number of nodes and number of edges are the same (n),
        # according to description, in tree for N node total edges N - 1
        uf = UnionFind(len(edges) + 1)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        return None
