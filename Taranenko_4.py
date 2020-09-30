########################### 1
my_list = [3, 7, 143, 13, 987]

for new_list in my_list:
    if new_list > 100:
        print(new_list)
########################### 2
my_list = []
n = int(input("Введите количество элементов: "))

for i in range(0, n):
    adding = int(input('Введите цифровые значения:'))
    my_list.append(adding)

print('My_results:')
my_results = []
for digits in my_list:
    if digits > 100:
        my_results.append(digits)
print(my_results)
########################### 3
my_list = [1, 3, 8, 11, 25]

# print(len(my_list))
if len(my_list) < 2:
    my_list.append(0)

elif len(my_list) >= 2:
    some_amount = (my_list[-1] + my_list[-2])
    my_list.append(some_amount)

print(my_list)
############################## 4
value = (input('Введите число:'))

try:
    value = float(value)
    result = value ** -1
except (ValueError, ZeroDivisionError):
    print('Вы ввели некорректные данные либо букву/символ!')
    result = None

print(result)
############################## 5
my_indexes = [0, 1, 2, 3, 4, 5]
my_list = 'dexter'
for index in my_indexes:
    print(my_list[index].title())
############################## 6
my_indexes = [0, 1, 2, 3]
my_list_1 = [1, 7, 13, 66]
my_list_2 = [3, 11, 26, 99]
for index in my_indexes:
    print((my_list_1[index], my_list_2[index]))
############################## 7
my_string = '0123456789'
my_string_1 = my_string
for new_string in my_string:
    for new_string_1 in my_string_1:
        print([new_string + new_string_1])
