def get_distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_size(a: tuple[int, ...], b: tuple[int, ...]) -> float:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def get_largest(pairs: list[tuple[int, ...]]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return max(((a, b) for i, a in enumerate(pairs) for b in pairs[i+1:]), key=lambda p: get_distance(*p))

def intersects(edges_h: list[tuple[int, int, int]], edges_v: list[tuple[int, int, int]], borders: list[int]) -> bool:
    top, right, bottom, left = borders

    for (edge_left, edge_right, edge_y) in edges_h:
        if top < edge_y < bottom and max(edge_left, left) < min(edge_right, right):
            return True

    for (edge_top, edge_bottom, edge_x) in edges_v:
        if left < edge_x < right and max(edge_top, top) < min(edge_bottom, bottom):
            return True

    return False

def build_edges(tiles: list[tuple[int, ...]]) -> tuple[list[tuple[int, int, int]], list[tuple[int, int, int]]]:
    edges_horizontal: list[tuple[int, int, int]] = []
    edges_vertical: list[tuple[int, int, int]] = []

    for i, tile in enumerate(tiles):
        tile_next = tiles[(i + 1) % len(tiles)]
        if tile[0] != tile_next[0]:
            edges_horizontal.append(
                (tile[0], tile_next[0], tile[1]) if tile[0] < tile_next[0] else (tile_next[0], tile[0], tile[1]))
        else:
            edges_vertical.append(
                (tile[1], tile_next[1], tile[0]) if tile[1] < tile_next[1] else (tile_next[1], tile[1], tile[0]))
    return edges_horizontal, edges_vertical

def find_largest_rectangle(tiles: list[tuple[int, ...]]) -> int:
    largest_seen = 0
    edges_horizontal, edges_vertical = build_edges(tiles)

    for i, tile_a in enumerate(tiles):
        for tile_b in tiles[i + 1:]:
            borders: list[int] = [min(tile_a[1], tile_b[1]), max(tile_a[0], tile_b[0]),  # top, right, bottom, left
                                  max(tile_a[1], tile_b[1]), min(tile_a[0], tile_b[0])]

            if not intersects(edges_horizontal, edges_vertical, borders):
                if get_size(tile_a, tile_b) > largest_seen:
                    largest_seen = get_size(tile_a, tile_b)

    return largest_seen

if __name__ == '__main__':
    with open('input.txt') as file:
        tiles_red: list[tuple[int, ...]] = [tuple(map(int, line.strip().split(','))) for line in file]

    largest_pair = get_size(*get_largest(tiles_red))
    print('Part one', largest_pair, largest_pair == 4750092396)

    largest_found = find_largest_rectangle(tiles_red)
    print('Part two', largest_found, largest_found == 1468516555)
