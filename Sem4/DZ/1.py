# Напишите функцию для транспонирования матрицы

"""Вариант 1"""
print ('Вариант 1')


import numpy 
matrix=numpy.array ([[1, 2, 4], [31, 17, 15], [41, 32, 234]])
matrix_trans=matrix.transpose()
print(matrix)
print(matrix_trans)

"""Вариант 2"""

print ('Вариант 2')


def matrix_trans2(*a_list: list[[]]) -> list[()] | str:
    trans = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            trans = False
    if trans:
        return list(zip(*a_list))


print(matrix_trans2([1, 2, 4], [31, 17, 15], [41, 32, 234]))
