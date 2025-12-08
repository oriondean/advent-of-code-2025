from math import sqrt, prod
from collections import deque

Box = tuple[int, int, int]

def build_nearest_neighbour_list(boxes: list[Box]) -> deque[tuple[Box, Box, float]]:
    nearest_neighbours = []

    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            nearest_neighbours.append((a, b, sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))))

    return deque(sorted(nearest_neighbours, key=lambda c: c[2]))

def connect_shortest(connections: dict[Box, list[Box]], shortest_distances: deque[tuple[Box, Box, float]], num: int) -> tuple[Box, Box]:
    for _ in range(num):
        (a, b, _) = shortest_distances.popleft()
        connections.setdefault(a, []).append(b)
        connections.setdefault(b, []).append(a)

    return a, b

def dfs(connections: dict[Box, list[Box]], node: Box, visited: set[Box], circuit: list[Box]) -> list[Box]:
    if node not in visited:
        visited.add(node)
        circuit.append(node)

        for neighbour in connections.get(node, []):
            if neighbour not in visited:
                dfs(connections, neighbour, visited, circuit)

    return circuit

def build_circuits(connections: dict[Box, list[Box]]) -> list[list[Box]]:
    visited: set[Box] = set()  # track all visited nodes, if already visited not a new circuit
    circuits: list[list[Box]] = []

    for box in connections:
        if box not in visited:
            circuits.append(dfs(connections, box, visited, []))  # visit all nodes building circuit

    return circuits

if __name__ == '__main__':
    with open('input.txt') as file:
        boxes: list[tuple[int, int, int]] = [tuple(map(int, line.strip().split(','))) for line in file]

    shortest_distances: deque[tuple[Box, Box, float]] = build_nearest_neighbour_list(boxes)
    connections: dict[Box, list[Box]] = {}
    connect_shortest(connections, shortest_distances, 1000)
    circuits: list[list[Box]] = build_circuits(connections)

    result_part_one = prod(len(c) for c in sorted(circuits, key=len, reverse=True)[:3])

    # Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit
    while len(circuits) > 1:
        (a, b) = connect_shortest(connections, shortest_distances, 1)
        circuits = build_circuits(connections)

    print('Part one', result_part_one, result_part_one == 97384)
    print('Part two', a[0] * b[0], a[0] * b[0] == 9003685096)
