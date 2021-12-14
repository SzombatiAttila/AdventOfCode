import matplotlib.pyplot as plt
import moviepy.editor as moviepy
import numpy as np


def get_max_x(char_input):
    return max(i[0] for i in char_input)


def get_max_y(char_input):
    return max(i[1] for i in char_input)


def next_folding(new_m, fold):
    orientation = fold[0]
    folding_line = fold[1]
    if orientation == 'y':
        for i in range(folding_line + 1, len(new_m)):
            for j in range(len(new_m[i])):
                if new_m[i][j] == 1:
                    new_m[folding_line - abs(folding_line - i)][j] = 1
        matrix = [new_m[i] for i in range(folding_line)]
    if orientation == 'x':
        for i in range(len(new_m)):
            for j in range(folding_line + 1, len(new_m[i])):
                if new_m[i][j] == 1:
                    new_m[i][folding_line - abs(folding_line - j)] = 1
        matrix = [[new_m[i][j] for j in range(folding_line)] for i in range(len(new_m))]
    return matrix


def count_hashtags(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count += 1
    return count


def solutions():
    with open('input.csv', 'r') as file:
        file_input = file.read().split('\n')
        char_input = [(int(i.split(',')[1]), int(i.split(',')[0])) for i in file_input if ',' in i]
        folding = [(fold.split('=')[0][-1], int(fold.split('=')[1])) for fold in file_input if 'along' in fold]
        matrix = [[0 for _ in range(get_max_y(char_input) + 1)] for _ in range(get_max_x(char_input) + 1)]
        for i, j in char_input:
            matrix[i][j] = 1
        filenames = []
        for idx, fold in enumerate(folding):
            next_matrix = next_folding(new_m=matrix, fold=fold)
            matrix = next_matrix
            if idx == 0:
                solution1 = count_hashtags(matrix=matrix)
            np_arr = np.array(matrix)
            filenames.append(f"solution{idx}.png")
            plt.imsave(f'solution{idx}.png', np_arr)

        def resize_func(t):
            if t <= 3:
                return 1 + 0 * t  # Zoom-in.
            elif 4 <= t <= 6:
                return 1 + 0.2 * t  # Stay.
            elif 7 <= t <= 8:
                return 1 + 0.4 * t  # Stay.
            else:
                return 1 + 0.8 * t  # Zoom-out.

        def make_gif():
            clips = [moviepy.ImageClip(i).set_duration(1).resize(resize_func(idx))
                     for idx, i in enumerate(filenames)]
            concat_clip = moviepy.concatenate_videoclips(clips, method="compose")
            concat_clip.write_gif("test.gif", fps=2)

        make_gif()

        return solution1


if __name__ == "__main__":
    first = solutions()
    print(f'The solution for the first part is : {first}')
