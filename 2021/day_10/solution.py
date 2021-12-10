from statistics import median

chunks_left_right = {"(": ")", "<": ">", "{": "}", "[": "]"}
chunks_right_left = {')': '(', '>': '<', '}': '{', ']': '['}

solution1_hash_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

solution2_hash_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def solutions():
    with open('input.csv', 'r') as file:
        char_input = [i for i in file.read().split('\n')]
        wrong_elem = []
        good_elem = []
        left_char_stack = []
        for elem in char_input:
            found = False
            for c in elem:
                if c in chunks_left_right.keys():
                    left_char_stack.append(c)
                else:
                    last_left = left_char_stack.pop()
                    if chunks_right_left[c] != last_left:
                        found = True
                        wrong_elem.append(c)
            if not found:
                good_elem.append(left_char_stack)
            left_char_stack = []
        solution2 = 0
        result = []
        for x in good_elem:
            for z in x[::-1]:
                solution2 = solution2 * 5 + solution2_hash_map[z]
            if solution2:
                result.append(solution2)
            solution2 = 0
        solution1 = sum(solution1_hash_map[i] for i in wrong_elem)
        return solution1, median(result)


if __name__ == "__main__":
    first, second = solutions()
    print(f'The solution for the first part is : {first}')
    print(f'The solution for the second part is : {second}')
