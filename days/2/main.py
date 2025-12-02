from utils.timer import timeit

def has_repeating_pattern(digits: str, length: int) -> bool:
    # Old slow way - using chunks (~x6 longer)
    # chunks: list[str] = [digits[i:i + length] for i in range(0, len(digits), length)]
    # return all(chunk == digits[0:length] for chunk in chunks)

    # New fast way - repeat pattern to match the length of digits and compare
    return digits == digits[:length] * (len(digits) // length)

@timeit
def find_invalid_ids(ranges_id: list[list[int]]) -> tuple[set[int], set[int]]:
    invalid_ids_half: set[int] = set()
    invalid_ids_any: set[int] = set()

    for start, end in ranges_id:
        for num in range(start, end + 1):
            num_str: str = str(num)
            size: int = len(num_str)

            # Search for repeating patterns from largest to smallest possible pattern size
            for size_pattern in range(size // 2, 0, -1):
                if not size % size_pattern and has_repeating_pattern(num_str, size_pattern):
                    invalid_ids_any.add(num)
                    if size_pattern == (size / 2):  # No // here to avoid odd sizes
                        invalid_ids_half.add(num)
                    break  # Match found, avoid checking smaller patterns

    return invalid_ids_half, invalid_ids_any


if __name__ == '__main__':
    with open('input.txt') as file:
        input_parsed: list[list[int]] = [list(map(int, line.split('-'))) for line in file.readlines()[0].split(',')]
    result: tuple[set[int], set[int]] = find_invalid_ids(input_parsed)

    print('Part one', sum(result[0]), sum(result[0]) == 44487518055)  # 44487518055
    print('Part two', sum(result[1]), sum(result[1]) == 53481866137)  # 53481866137