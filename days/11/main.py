def dfs_count_paths(graph: dict[str, list[str]], node: str, target: str, memo: dict[str, int]) -> int:
    if node == target:
        return 1  # one direct path left to target
    elif node in memo:
        return memo[node]  # already counted paths from this node to target

    memo[node] = sum([dfs_count_paths(graph, child, target, memo) for child in graph.get(node, [])])
    return memo[node]

if __name__ == '__main__':
    graph: dict[str, list[str]] = {}

    with open('input.txt') as file:
        for line_raw in file:
            (key, values) = line_raw.strip().split(': ')
            graph[key] = values.split(' ')

    print('Part one', dfs_count_paths(graph, 'you', 'out', {}), dfs_count_paths(graph, 'you', 'out', {}) == 543)

    # The graph is directed acyclic graph (DAG)
    # There are no paths from 'dac' to 'fft' but there are paths from 'fft' to 'dac'
    # All valid paths go through 'svr' -> 'fft' -> 'dac' --> 'out'
    paths_valid = (dfs_count_paths(graph, 'svr', 'fft', {}) * dfs_count_paths(graph, 'fft', 'dac', {}) *
                   dfs_count_paths(graph, 'dac', 'out', {}))
    print('Part two', paths_valid, paths_valid == 479511112939968)
