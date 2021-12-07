def generate_matrix(length):
    return [['.' for _ in range(length)] for _ in range(length)]

def same_point(point):
    first_part = point[0].split(',')
    second_part = point[1].split(',')
    if first_part[0] == second_part[0]:
        return 'row'
    elif first_part[1] == second_part[1]:
        return 'col'
    else:
        return 'diagonal'


def is_horizontal(point):
    x1 = point[0].split(',')[0]
    x2 = point[1].split(',')[0]
    return x1 == x2


def is_vertical(point):
    y1 = point[0].split(',')[1]
    y2 = point[1].split(',')[1]
    return y1 == y2


def is_diagonal(point):
    x1 = point[0].split(',')[0]
    x2 = point[1].split(',')[0]
    y1 = point[0].split(',')[1]
    y2 = point[1].split(',')[1]
    return abs(int(x1) - int(x2)) == abs(int(y1) - int(y2))


def get_range(point, col_or_row):
    if col_or_row == 'col':
        x1 = int(point[0].split(',')[0])
        x2 = int(point[1].split(',')[0])
        if x1 > x2:
            return range(x1, x2 - 1, -1)
        return range(x1, x2 + 1)
    elif col_or_row == 'row':
        y1 = int(point[0].split(',')[1])
        y2 = int(point[1].split(',')[1])
        if y1 > y2:
            return range(y1, y2 - 1, -1)
        return range(y1, y2 + 1)
    elif col_or_row == 'diagonal':
        # 1, 1 -> 3, 3 -> (1,1), (2,2), (3,3)
        # 9, 7 -> 7, 9 -> (9.7), (8,8), (7,9)
        arr = []
        x1 = int(point[0].split(',')[0])
        x2 = int(point[1].split(',')[0])
        y1 = int(point[0].split(',')[1])
        y2 = int(point[1].split(',')[1])
        if y1 > y2:
            arr.append(range(y1, y2 - 1, -1))
        else:
            arr.append(range(y1, y2 + 1))
        if x1 > x2:
            arr.append(range(x1, x2 - 1, -1))
        else:
            arr.append(range(x1, x2 + 1))
        return arr


def get_point_list(point_tuple):
    get_same_point = same_point(point_tuple)
    ranges = get_range(point_tuple, get_same_point)

    if get_same_point == 'row':
        return [(int(point_tuple[0].split(',')[0]), i) for i in ranges]
    elif get_same_point == 'col':
        return [(i, int(point_tuple[1].split(',')[1])) for i in ranges]
    elif get_same_point == 'diagonal':
        return [i for i in zip(ranges[1], ranges[0])]


def solutions(solution_2):
    with open('input.csv', 'r') as file:
        file_input = [tuple(value.split(' -> ')) for value in file.read().splitlines()]
        matrix = generate_matrix(1000)
        get_dangerous_point_num = 0
        for line in file_input:
            if is_horizontal(line) or is_vertical(line) or (is_diagonal(line) and solution_2):
                point_list = get_point_list(line)
                for elem in point_list:
                    if matrix[elem[1]][elem[0]] != '.':
                        matrix[elem[1]][elem[0]] = str(int(matrix[elem[1]][elem[0]]) + 1)
                    elif matrix[elem[1]][elem[0]] == '.':
                        matrix[elem[1]][elem[0]] = '1'
        for i in matrix:
            for j in i:
                if j != '.':
                    if int(j) >= 2:
                        get_dangerous_point_num += 1
        return get_dangerous_point_num


if __name__ == "__main__":
    first = solutions(solution_2=False)
    second = solutions(solution_2=True)
    print(f'The solution for the first part is : {first}')
    print(f'The solution for the second part is : {second}')
