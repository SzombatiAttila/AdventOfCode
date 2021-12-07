import statistics

from utils.decorators import measure_time_sync


@measure_time_sync
def solutions2():
    with open('input.csv', 'r') as file:
        life_input = [int(i) for i in file.read().split(',')]
        max_range = max(life_input)
        min_val = min(
            sum((elem - cost + 1) * (elem - cost) // 2 for elem in life_input) for cost in range(max_range))
        return min_val


def solutions1():
    with open('input.csv', 'r') as file:
        life_input = [int(i) for i in file.read().split(',')]
        med = statistics.median(life_input)
        return sum(abs(i - med) for i in life_input)


if __name__ == "__main__":
    first = solutions1()
    second = solutions2()
    print(f'The solution for the first part is : {first}')
    print(f'The solution for the second part is : {second}')
