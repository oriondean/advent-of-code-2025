from math import floor

if __name__ == '__main__':
    position: int = 50
    zero_count_p1: int = 0
    zero_count_p2: int = 0

    with open('input.txt') as file:
        for line in file:
            moves = int(line.strip()[1:])
            delta = moves * (1 if line[0] == 'R' else -1)

            # Detect zero crossings for part two
            if (position != 0 or abs(delta) >= 100) and not (0 < position + delta < 100):
                position_new = position + delta
                times_zeroed = max(abs(floor(position_new / 100)), 1)

                if position_new <= -100 and position_new % 100 == 0:
                    times_zeroed += 1 # handle case where we land exactly on zero going negative
                elif position == 0 and position_new < -100:
                    times_zeroed -= 1 # handle case where we start on zero and go negative over 100

                zero_count_p2 += times_zeroed

            position = (position + delta) % 100

            if position == 0:
                zero_count_p1 += 1
        file.close()

    print('Part one', zero_count_p1) # 1092
    print('Part two', zero_count_p2) # 6616