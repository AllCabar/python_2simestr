# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
# строковое представление. Функцию hex используйте для проверки своего результата.


number = int(input('Введите число:'))
base = 16
letters = '0123456789abcdef'
new_number = ''
test_number=number 
while number > 0:
    number, remainder = divmod(number, base)
    new_number = letters[remainder] + new_number
 
print('Число в 16ти ричной системе:',new_number,'   Проверка:',hex(test_number)[2:])
