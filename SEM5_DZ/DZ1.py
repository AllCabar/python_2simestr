# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

put = input ('Введите путь до документа:')


def fun1(put: str) -> tuple():
    put_2 = put.split('\\')
    last_elem = put_2[-1].split('.')
    path = '\\'.join(put_2[0:-1])
    name = last_elem[0]
    expansion = last_elem[1]
    return path, name, expansion


print(fun1(put))