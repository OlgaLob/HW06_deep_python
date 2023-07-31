# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


import itertools

# _QUEEN_COUNT: int = 8  # максимальное кол-во ферзей
# _SIZE_BOARD: int = 8  # размер доски
COLS = 'abcdefgh'
ROWS = '12345678'


#
# def generate_combinations():
#     nums = list(range(1, 9))  # список чисел от 1 до 8
#     combi = list(itertools.combinations(nums, 2))  # все возможные комбинации из 2 элементов
#     combi_ferz = []
#     for item in itertools.permutations(combi, 8):
#         combi_ferz.append(item)
#     # random_combinations = list(combinations(combi, n))  # случайные комбинации из n элементов
#     for item in combi_ferz:
#         if check_queen_8x8(combi_ferz):
#             print(combi_ferz)
#             return combi_ferz
#
#
# def check_queen_8x8(positions: list[tuple]) -> bool:
#     result = True
#
#     if len(positions) != _QUEEN_COUNT:
#         result = False
#     else:
#         for i in range(_QUEEN_COUNT - 1):  # берем ферзей по списку, исключая последнего (сам себя бить не может)
#             if not result:
#                 break
#             row_1, col_1 = positions[i]
#             for j in range(i + 1, _QUEEN_COUNT):  # проверяем со следующими до конца списка
#                 row_2, col_2 = positions[j]
#                 # Ферзи на одной линии, если координаты строки или столбца у них равны.
#                 # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением на равное
#                 # количество строк и столбцов в любую из сторон
#                 if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
#                     result = False
#                     break
#
#     return result


def check_qweens(arr: list[tuple[int, int]]) -> bool:
    for i in range(len(arr)):
        row_prev, col_prev = arr[i]
        for j in range(i + 1, len(arr)):
            row_next, col_next = arr[j]
            if (
                    row_prev == row_next or
                    col_prev == col_next or
                    abs(row_prev - row_next) == abs(col_prev - col_next)
            ):
                return False
    print(arr)
    return True


def generate_combinations():
    win_combs = set()
    coord_pack = []
    for comb in itertools.permutations(COLS):
        coord_pack.append([(COLS.find(pair[0]), ROWS.find(pair[1])) for pair in zip(comb, ROWS)])
    for pack in coord_pack:
        if check_qweens(pack):
            win_combs.add(tuple(pack))
    return win_combs


if __name__ == '__main__':
    win_placements = generate_combinations()
    print(len(win_placements))
