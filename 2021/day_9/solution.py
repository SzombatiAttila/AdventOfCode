from numpy import prod

def generate_matrix(matrix):
    return [[int(i) for i in col] for col in matrix]


def hash_table(matrix):
    return [[False for _ in col] for col in matrix]


with open('input.csv', 'r') as file:
    life_input = [i for i in file.read().split('\n')]
    matrix = generate_matrix(life_input)
    visited_points = hash_table(matrix)


def is_lowest(i, j, matrix):
    if 0 <= i < len(matrix) - 1 and 0 <= j < len(matrix[0]) - 1:
        up = matrix[i - 1][j]
        down = matrix[i + 1][j]
        left = matrix[i][j - 1]
        right = matrix[i][j + 1]
        min_val = min([up, down, left, right])
        if min_val > matrix[i][j]:
            return matrix[i][j]


def rec(i, j, matrix):
    if matrix[i][j] < 9 and visited_points[i][j] is False:
        visited_points[i][j] = True
        yield 1
        yield from rec(i - 1, j, matrix)
        yield from rec(i, j - 1, matrix)
        yield from rec(i + 1, j, matrix)
        yield from rec(i, j + 1, matrix)
    else:
        yield 0


def solutions2():
    with open('input.csv', 'r') as file:
        life_input = [i for i in file.read().split('\n')]
        matrix = generate_matrix(life_input)
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                low_num = is_lowest(i, j, matrix)
                if low_num or low_num == 0:
                    get_nums = sum(i for i in rec(i, j, matrix))
                    arr.append(get_nums)
        return prod(sorted(arr)[::-1][:3])


def solutions1():
    with open('input.csv', 'r') as file:
        life_input = [i for i in file.read().split('\n')]
        matrix = generate_matrix(life_input)
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                low_num = is_lowest(i, j, matrix)
                if low_num or low_num == 0:
                    arr.append(low_num + 1)
        return sum(arr)


if __name__ == "__main__":
    first = solutions1()
    second = solutions2()
    print(f'The solution for the first part is : {first}')
    print(f'The solution for the second part is : {second}')
