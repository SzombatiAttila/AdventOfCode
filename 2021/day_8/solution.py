def is_substring(one, two):
    try:
        return all(i in two for i in one)
    except TypeError:
        print(f'{one=} and {two=}')


def set_easy_values(hash_map, easy_values):
    easy_values.sort(key=len)
    for easy in easy_values:
        x = ''.join([i for i in sorted(easy)])
        if len(easy) == 2:
            hash_map[1] = x
        elif len(easy) == 3:
            hash_map[7] = x
        elif len(easy) == 4:
            hash_map[4] = x
        elif len(easy) == 7:
            hash_map[8] = x
    return hash_map


def generate_hash_map(hash_t, elem):
    elem.sort(key=len)
    for x in elem:
        x = ''.join([i for i in sorted(x)])
        if len(x) == 6:
            if not is_substring(hash_t[1], x):
                hash_t[6] = x
            elif is_substring(hash_t[4], x):
                hash_t[9] = x
            else:
                hash_t[0] = x
        elif len(x) == 5:
            asd = ''.join([i for i in sorted((set(x + hash_t[4])))])
            if asd == hash_t[8]:
                hash_t[2] = x
            elif is_substring(hash_t[1], x):
                hash_t[3] = x
            else:
                hash_t[5] = x
    return hash_t


def solutions1():
    with open('input.csv', 'r') as file:
        life_input = [[len(i) for i in i.split(' | ')[1].split(' ')] for i in file.read().split('\n')]
        asd = {n: 0 for n in range(9)}
        for elem in life_input:
            for j in elem:
                asd[j] += 1
        return asd[2] + asd[4] + asd[3] + asd[7]


def solutions2():
    with open('input.csv', 'r') as file:
        input_file = [[i for i in i.split(' | ')] for i in file.read().split('\n')]
        inputs = [i[0].split(' ') for i in input_file]
        outputs = [i[1].split(' ') for i in input_file]
        res = 0
        for elem, out in zip(inputs, outputs):
            hash_m = {n: 0 for n in range(10)}
            easy_values = [i for i in elem if len(i) in [2, 3, 4, 7]]
            hash_map_with_easy_values = set_easy_values(hash_m, easy_values)
            h_map = {i: j for j, i in generate_hash_map(hash_map_with_easy_values, elem).items()}
            res_sum = ""
            for result in out:
                sorted_output_elem = ''.join([i for i in sorted(result)])
                if sorted_output_elem in h_map:
                    res_sum += str(h_map[sorted_output_elem])
            if res_sum:
                res += int(res_sum)
        return res


if __name__ == "__main__":
    first = solutions1()
    second = solutions2()
    print(f'The solution for the first part is : {first}')
    print(f'The solution for the second part is : {second}')
