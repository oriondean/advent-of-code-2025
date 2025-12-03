def find_highest_digits(digits: list[int]) -> str:
    for i in range(9, 0, -1):
        if i in digits and digits.index(i) < len(digits) - 1:
            for j in range(9, 0, -1):
                if j in digits and len(digits) - 1 - digits[::-1].index(j) > digits.index(i):
                    return str(i) + str(j)

    return '0'

def switch_leftmost_highest(digits: list[tuple[int, bool]], start: int, end: int) -> int:
    for number in range(9, 0, -1):
        for i in range (start, len(digits) + end):
            if digits[i][0] == number:
                digits[i] = (digits[i][0], True)
                return i
    return -1

if __name__ == '__main__':
    with open('input.txt') as file:
        batteries: list[list[int]] = [list(map(int, x.strip())) for x in file.readlines()]

    joltage_max_pair: int = 0
    joltage_max_twelve: int = 0

    for bank in batteries:
        joltage_max_pair += int(find_highest_digits(bank))
        switches = [(b, False) for b in bank]

        start: int = 0
        for end in range(-11, 1):
            switched = switch_leftmost_highest(switches, start, end)
            start = switched + 1 # next search starts _after_ the last switched battery

        joltage_max_twelve += int(''.join([str(x[0]) for x in switches if x[1]]))

    print('Part one', joltage_max_pair, joltage_max_pair == 17155)
    print('Part two', joltage_max_twelve, joltage_max_twelve == 169685670469164)