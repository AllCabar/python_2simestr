# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.


def my_fun(**kwargs):
    result = {}
    for key, value in kwargs.items():
         if isinstance(value, (list, dict, set, bytearray)):
                value = str(value)
         result[value] = key
    return result


print(my_fun(name='Шатров Федор', bal=4.8,work='Ученик', school=6,))
