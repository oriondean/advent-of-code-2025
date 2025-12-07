if __name__ == '__main__':
    with open('input.txt') as file:
        grid: list[list[str]] = [list(line.strip()) for line in file]

    beams: set[int] = {grid[0].index('S')}
    timelines: list[dict[int, int]] = [{} for _ in range(len(grid))]
    split_count: int = 0

    for i, row in enumerate(grid):
        to_remove: set[int] = set()

        for beam in beams:
            if row[beam] in '.S':
                row[beam] = '|'
                timelines[i][beam] = timelines[i].get(beam, 0) + (timelines[i - 1].get(beam, 0) if i > 0 else 1)
            elif row[beam] == '^':
                split_count += 1
                to_remove.add(beam)
                previous_value = timelines[i - 1][beam]

                for offset in (-1, 1): # split left and right
                    col = beam + offset
                    timelines[i][col] = previous_value if row[col] == '.' else previous_value + timelines[i][col]
                    row[col] = '|'
            elif row[beam] == '|':
                timelines[i][beam] += timelines[i - 1][beam]

        beams -= to_remove
        beams |= {beam + offset for beam in to_remove for offset in (-1, 1)} # add new beams

    print('Part one', split_count, split_count == 1658)
    print('Part two', sum(timelines[-1].values()), sum(timelines[-1].values()) == 53916299384254)