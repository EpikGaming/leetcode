def findRedundantConnection(edges: list):
    nodesCount = len(edges)
    parent = list(range(nodesCount + 1))
    def find(index: int):
        if parent[index] != index:
            parent[index] = find(parent[index])
        return parent[index]

    def union(index1: int, index2: int):
        parent[find(index1)] = find(index2)

    for node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
        else:
            print(parent)
            return [node1, node2]
    return []


test = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(findRedundantConnection(test))