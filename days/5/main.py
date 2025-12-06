def parse_input(lines: list[str]) -> tuple[list[range], list[str]]:
    ranges: list[range] = []
    ingredients: list[str] = []
    parsing_ranges: bool = True

    for line_raw in lines:
        line: str = line_raw.strip()
        if line == '':
            parsing_ranges = False
        else:
            if parsing_ranges:
                (start, end) = map(int, line.split('-'))
                ranges.append(range(start, end + 1))
            else:
                ingredients.append(line)

    return ranges, ingredients

def merge_ranges(to_merge: list[range]) -> tuple[list[range], bool]:
    merge_occurred: bool = False

    for i, r in enumerate(to_merge):
        ranges_overlapping: list[range] = [s for s in to_merge if r.start in s and r != s]

        if any([s for s in to_merge if r.start >= s.start and r.stop <= s.stop and r != s]):
            to_merge.remove(r)
        elif any(ranges_overlapping):
            new_start = max([s.stop for s in ranges_overlapping]) # get latest start from all overlaps
            to_merge[i] = range(new_start, r.stop) if new_start < r.stop else range(new_start, r.stop)
            merge_occurred = True

    return list(set(to_merge)), merge_occurred # dedupe ranges

if __name__ == '__main__':
    with open('input.txt') as file:
        (fresh_ranges, ingredients) = parse_input(file.readlines())

    count_fresh_ingredients = len([i for i in ingredients if any([r for r in fresh_ranges if int(i) in r])])

    merging_required = True
    while merging_required:
        fresh_ranges, merging_required = merge_ranges(fresh_ranges)

    print('Part one - available fresh ingredients', count_fresh_ingredients)
    print('Part two - all possible fresh ingredients', sum([r.stop - r.start for r in fresh_ranges]))