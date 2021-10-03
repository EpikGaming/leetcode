from collections import defaultdict

def calcEquation(equations: list, values: list, queries: list):
    graph = defaultdict(int)
    set1 = set()
    for i in range(len(equations)):
        a, b = equations[i]
        graph[(a, b)] = values[i]
        graph[(b, a)] = 1 / values[i]
        set1.add(a)
        set1.add(b)

    arr = list(set1)
    for k in arr:
        for i in arr:
            for j in arr:
                if graph[(i, k)] and graph[(k, j)]:
                    graph[(i, j)] = graph[(i, k)] * graph[(k, j)]

    result = []
    for x, y in queries:
        if graph[(x, y)]:
            result.append(graph[(x, y)])
        else:
            result.append(-1)

    return result
