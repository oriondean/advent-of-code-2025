from re import compile, Pattern

if __name__ == '__main__':
    with open('input.txt') as file:
        lines: list[str] = [i.strip() for i in file.readlines()]

    shapes: list[list[str]] = [[c.replace('#', '') for c in lines[i + 1:i + 4]] for i in range(0, 30, 5)]
    pattern: Pattern[str] = compile('(\d+)x(\d+): ([\d\s]+)')
    areas = [
        tuple([int(h), int(w)] + [[int(c) for c in counts.split()]])
        for h, w, counts in (pattern.match(puzzle).groups() for puzzle in lines[30:])
    ]

    # really simple area check does it... no 2d bin packing needed :((
    count = len([area for area in areas if area[0] * area[1] >= sum(area[2]) * 7])
    print('Part one', count, count == 463)
