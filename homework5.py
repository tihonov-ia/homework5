#Кортеж
immutable_var = (1, 2, 'a', 'b')
print('Immutable tuple: ', immutable_var)
#immutable_var[1] = 100 - попытка изменения выдаёт ошибку.
#Кортеж не поддерживает обращение по элементам, можем выводить, добавлять или повторять значения.

#Создание изменяемых структур данных
mutable_list = [1, 2, 'a', 'b', ]
mutable_list[3] = "Modified"
print('Mutable list: ', mutable_list)