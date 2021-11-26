graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if not v in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(f'recursive_dfs: {recursive_dfs(1)}')
print(f'iterative_dfs: {iterative_dfs(1)}')