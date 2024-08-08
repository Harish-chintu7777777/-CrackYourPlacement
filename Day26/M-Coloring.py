def isSafe(node, color, graph, n, col):
    for k in range(n):
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True


def solve(node, color, m, N, graph):
    if node == N:
        return True


    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node + 1, color, m, N, graph):
                return True
            color[node] = 0


    return False

def graphColoring(graph, m, N):
    color = [0] * N
    if solve(0, color, m, N, graph):
        return True
    return False
