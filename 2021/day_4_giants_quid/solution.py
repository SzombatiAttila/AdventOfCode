def is_row_all_int(j):
    return all(isinstance(i, int) for i in j)


def is_column_all_int(idx, lines_arr):
    return all(isinstance(k, int) for k in [[i[j] for i in lines_arr] for j in range(5)][idx])


def get_number(random_input, str_parts):
    arr = []
    solution_1_found = False
    solution_1_arr = []
    for inp in random_input.split(','):
        for idx_i, i in enumerate(str_parts):
            for j in i:
                for idx_j, k in enumerate(j):
                    if k == str(inp):
                        j[idx_j] = int(k)
                    if is_row_all_int(j) or is_column_all_int(idx_j, i):
                        if not solution_1_found:
                            solution_1_found = True
                            unmarked_sum = sum(sum(int(j) for j in k if isinstance(j, str)) for k in i)
                            solution_1_arr.extend([inp, unmarked_sum])
                        if idx_i not in arr:
                            arr.append(idx_i)
                        elif len(arr) == len(str_parts):
                            return arr, str_parts[idx_i], inp, solution_1_arr


def get_unmarked_numbers(parts):
    return sum(sum(int(k) for k in i if isinstance(k, str)) for i in parts)


def solutions():
    with open('input.csv', 'r') as file:
        file_input = [value for value in file.read().splitlines()]
        guesses_input = file_input[0]
        table = [i for i in file_input[1:] if i != '']
        parts = [table[i:i + 5] for i in range(0, len(table), 5)]
        str_elems = [[c.split() for c in part] for part in parts]
        num = get_number(guesses_input, str_elems)
        number = get_unmarked_numbers(num[1])
        print(f'The solution for the first part is : {num[-1][-1] * int(num[-1][0])}')
        print(f'The solution for the second part is : {number * int(num[-2])}')


if __name__ == "__main__":
    solutions()
