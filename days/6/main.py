from functools import reduce
from re import compile

def solve_part_one(problem: list[list[str]]) -> int:
    problems = 0
    for col in range(0, len(problem[0])):
        numbers = [int(problem[row][col]) for row in range(0, len(problem) - 1)]
        problems += calc_problem(numbers, problem[len(problem) - 1][col])

    return problems

def solve_part_two(grid: list[list[str]]) -> int:
    sum_problems = []
    numbers_problem = []
    operator = ''
    number_rows = len(grid) - 1 # last row is operators

    for col in range(0,  max([len(r) for r in grid])):
        number_raw = ''

        if col < len(grid[number_rows]) and grid[number_rows][col] in ['*', '+']:
            operator = grid[number_rows][col]

        for row in range(0, number_rows): # magic number 4 largest number
            if col < len(grid[row]):
                number_raw += grid[row][col]

        if number_raw.strip() == '': # encountered empty column, next problem...
            sum_problems += calc_problem(numbers_problem, operator),
            numbers_problem = []
        else:
            numbers_problem += int(number_raw),

    sum_problems += calc_problem(numbers_problem, operator), # last problem

    return sum(sum_problems)

def calc_problem(numbers: list[int], operator: str) -> int:
    return sum(numbers) if operator == '+' else reduce((lambda x, y: x * y), numbers)

if __name__ == '__main__':
    pattern = compile('\s+')

    with open('input.txt') as file:
        input_raw = file.readlines()

    result_part_one = solve_part_one([pattern.split(line.strip()) for line in input_raw])
    result_part_two = solve_part_two([list(x.rstrip()) for x in input_raw])

    print('Part one', result_part_one, result_part_one == 4722948564882)
    print('Part two', result_part_two, result_part_two == 9581313737063)