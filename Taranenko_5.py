################################# 1
number = 10579085700
digit = 0
count = str(number).count(str(digit))
print(int(count))

################################# 2
number_1 = 10575555908570000
number_1 = str(number_1)
print(int(len(number_1)) - len(number_1.rstrip('0')))

################################# 3
my_list_1 = [1,2,3,4,5]
my_list_2 = [10,15,20,25]
new_list_1 = [value for value in my_list_1 if not value % 2]
new_list_2 = [value for value in my_list_2 if  value % 2]
my_result = new_list_1 + new_list_2
print(my_result)

################################# 4
my_list = [1, 2, 3, 4]
new_list = []
str_index = [1, 2, 3, 0]
for index in str_index:
    symbol = my_list[index]
    new_list.append(symbol)
print(new_list)

################################# 5
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

################################ 6 (долгий и глупый вариант решения)
my_str = '43 больше чем 34 но меньше чем 56'
new_str = []
zero = 0
while zero < len(my_str):
    digits = ''
    some = my_str[zero]
    while '0' <= some <= '9':
        digits += some
        zero += 1
        if zero < len(my_str):
            some = my_str[zero]
        else:
            break
    zero += 1
    if digits != '':
        new_str.append(int(digits))
print(sum(new_str))
################################## 6 (быстрый и разумный вариант решения))
my_str = '43 больше чем 34 но меньше чем 56'
new_str = [int(digits) for digits in my_str.split() if digits.isdigit()]
print(sum(new_str))

################################# 7
my_str = 'abcdef'
if len(my_str) % 2 == 0:
    print([my_str[symbol: symbol + 2] for symbol in range(0, len(my_str), 2)])
else:
    my_str = my_str + '_'
    print([my_str[symbol: symbol + 2] for symbol in range(0, len(my_str), 2)])
################################# 8
my_str = 'My_long str'
l_limit = 'o'
r_limit = 't'
sub_str = my_str[my_str.find(l_limit)+1:my_str.find(r_limit):]
print(sub_str)
################################# 9
my_str = 'My_long string'
l_limit = 'o'
r_limit = 'g'
sub_str = my_str[my_str.find(l_limit)+1:my_str.rfind(r_limit):]
print(sub_str)
################################# 10
digits = [2,4,1,5,3,9,0,7]
answer = 0
for value in range(1, len(digits) - 1):
    if digits[value - 1] < digits[value] > digits[value+1]:
        answer += 1
print(answer)
