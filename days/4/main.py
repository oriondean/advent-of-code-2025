def count_adjacent_rolls(grid: list[list[str]], row: int, col: int) -> int:
    adjacent: int = 0
    directions: list[tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '@':
            adjacent += 1

    return adjacent

if __name__ == '__main__':
    removed: list[int] = []

    with open('input.txt') as file:
        grid: list[list[str]] = [list(line.strip()) for line in file.readlines()]

    while not removed or removed[-1] > 0:
        to_remove: list[tuple[int, int]] = []

        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == '@':
                    if count_adjacent_rolls(grid, y, x) < 4:
                        to_remove.append((x, y))

        for coord in to_remove:
            grid[coord[1]][coord[0]] = 'x'
        removed.append(len(to_remove))

    print('Part one', removed[0], removed[0] == 1363)
    print('Part two', sum(removed), sum(removed) == 8184)