# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import time
import random as rnd
import logging
import argparse

def check(my_qeens: tuple) -> True | False:
    """ Проверка на наличие пары, бьющей друг друга"""
    for i in range(len(my_qeens)-1):
        for j in range(i+1, len(my_qeens)):
            if my_qeens[i][0] == my_qeens[j][0] or my_qeens[i][1] == my_qeens[j][1] or \
                abs(my_qeens[i][0]- my_qeens[j][0]) == abs(my_qeens[i][1]-my_qeens[j][1]):
                return False
    return True        


def queens_setup(queens_number: int = 2, chessboard_size: int = 8) -> tuple:
    """ Генерация расстановки ферзей """
    queens_set = set()
    for i in range(1, queens_number + 1):
        queens_set.add((i, rnd.randint(1, chessboard_size)))
    return tuple(queens_set)

if __name__ =="__main__":
    FORMAT = '{levelname:<6}, {asctime}, {name}, {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='queens.log', filemode='w', encoding='utf-8', level=logging.INFO)
    # Каждый раз создаем новый пустой файл
    logger = logging.getLogger('queens')    

    parser = argparse.ArgumentParser(description="Solving task of queens' cheese. ")
    parser.add_argument('-q_n', metavar='q_n', type=int, help='QUEENS_NUMBER', default=8)
    parser.add_argument('-n_s', metavar='n_s', type=int, help='NUMBER_OF_SET', default=4)
    parser.add_argument('-ch_s', metavar='ch_s', type=int, help='CHESSBOARD_SIZE', default=8)
    args = parser.parse_args()


    QUEENS_NUMBER = args.q_n
    NUMBER_OF_SET = args.n_s
    CHESSBOARD_SIZE = args.ch_s

    start_time = time.time()

    logger.info(f'{time.asctime()}')    
    logger.info(f' Solving task of queens cheese QUEENS_NUMBER = {QUEENS_NUMBER} \
NUMBER_OF_SET = {NUMBER_OF_SET} CHESSBOARD_SIZE = {CHESSBOARD_SIZE}')

    count = 0
    # dic_queens = {}

    while count != NUMBER_OF_SET:
        queens = queens_setup(QUEENS_NUMBER, CHESSBOARD_SIZE)
        while not check(queens):
            queens = queens_setup(QUEENS_NUMBER, CHESSBOARD_SIZE)
        count += 1
        print(f'Найдено {count}')
        # dic_queens[count] = queens
        logger.info(f'{count} = {queens}')

    # print(dic_queens)

    end_time = time.time()
    delta_time = end_time - start_time
    logger.info(f'Сode execution duration (seconds) {delta_time}')
    print(f'Время выполнения кода {delta_time}')
    logger.info(f'{time.asctime()}')