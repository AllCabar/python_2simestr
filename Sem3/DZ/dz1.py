# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

list = [6,7,3,8,6,5,1,3,5,9,0,5,3,1,5,5]
duplicat = set()
repeated = set()

for i in list:
    if i in duplicat:
        repeated.add(i)
    else:
        duplicat.add(i)
print(repeated)