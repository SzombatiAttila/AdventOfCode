from collections import Counter


def generate_life(life_input, prev_day):
    return [life - 1 if life - 1 >= 0 else 6 for life in life_input] + [8 for _ in range(Counter(prev_day)[0])]


def solutions_slow():
    max_life = 8
    with open('input.csv', 'r') as file:
        life_input = [int(i) for i in file.read().split(',')]
        for day in range(max_life):
            prev_day = life_input
            tmp_life_input = life_input
            life_input = generate_life(tmp_life_input, prev_day)
        return life_input


def solutions_fast(number_of_days):
    max_life = 8
    with open('input.csv', 'r') as file:
        life_input = [int(i) for i in file.read().split(',')]
        fish_dict = {n: life_input.count(n) for n in range(max_life + 1)}
    for day in range(number_of_days):
        new_fish = fish_dict[0]
        for i in range(max_life):
            fish_dict[i] = fish_dict[i + 1]
            fish_dict[i + 1] = 0
        fish_dict[6] += new_fish
        fish_dict[8] += new_fish

    return sum(fish_dict.values())


if __name__ == "__main__":
    first = solutions_fast(number_of_days=80)
    second = solutions_fast(number_of_days=256)
    print(f'The solution for the first part is : {first}')
    print(f'The solution for the second part is : {second}')
