import random
from random import randint

############################## 1
rand_list = [randint(1, 100) for _ in range(random.randint(20, 20))]
print(f'1:', rand_list)

############################### 2
this_A = tuple([randint(1, 100) for _ in range(random.randint(3, 3))])
this_B = tuple([randint(1, 100) for _ in range(random.randint(3, 3))])
this_C = tuple([randint(1, 100) for _ in range(random.randint(3, 3))])
triangle = dict(A = this_A, B = this_B, C = this_C)
print(f'2:', triangle)

############################## 3
my_str = 'Hello, my name is Dexter Morgan!'
def my_print():
    print(f'3:', '***'+my_str+'***')
my_print()

############################## 4 (a)
my_dict_1 = {'key_1':  '11', 'key_2':  '26', 'key_4':  '5', 'key_6':  '26'}
my_dict_2 = {'key_1':  '666', 'key_3':  '8', 'key_5':  '25', 'key_6':  '13'}
my_list = [key for key in my_dict_1.keys() if key in my_dict_2.keys()]
print(f'4(а):', my_list)

############################## 4 (б)
my_dict_1 = {'key_1':  '11', 'key_2':  '26', 'key_4':  '5', 'key_6':  '26'}
my_dict_2 = {'key_1':  '666', 'key_3':  '8', 'key_5':  '25', 'key_6':  '13'}
my_list = [key for key in my_dict_1.keys() if key not in my_dict_2.keys()]
print(f'4(б):', my_list)

############################## 4 (в)
my_dict_1 = {'key_1':  '11', 'key_2':  '26', 'key_4':  '5', 'key_6':  '26'}
my_dict_2 = {'key_1':  '666', 'key_3':  '8', 'key_5':  '25', 'key_6':  '13'}
my_dict_3 = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2.keys():
        my_dict_3[key] = value
print(f'4(в):', my_dict_3)

############################## 4 (г)
my_dict_1 = {'key_1':  '11', 'key_2':  '26', 'key_4':  '5', 'key_6':  '26'}
my_dict_2 = {'key_1':  '666', 'key_3':  '8', 'key_5':  '25', 'key_6':  '13'}
my_dict_3 = {}
for key in (my_dict_1.keys() | my_dict_2.keys()):
    if key in my_dict_1: my_dict_3.setdefault(key, []).append(my_dict_1[key])
    if key in my_dict_2: my_dict_3.setdefault(key, []).append(my_dict_2[key])
print(f'4(г):', my_dict_3)
