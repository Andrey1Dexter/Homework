############################### 1
my_list = ['Hello', 'my', 'name', 'Dexter', 'Morgan']
new_list = []
for change, some in enumerate(my_list):
    if change % 2 != 0:
       new_list.append(some[::-1])
    else:
        new_list.append(some)
print(f'1.', new_list)

################################# 2
my_list = ['чубака', 'Азазель', 'кентавр', 'антилопа', 'лось', 'конь', 'зебра']
new_list = [value for value in my_list if value.startswith('А') or value.startswith('а')]
print(f'2.', new_list)

################################# 3
my_list = ['чубака', 'Азазель', 'кентавр', 'антилопа', 'лось', 'конь', 'зебра']
new_list = [value for value in my_list if 'а' in value or 'А' in value ]
print(f'3.', new_list)

################################# 4
my_list = ['du', 2, 'du', 3, 'hast', 4, 'mich', 1]
new_list = []
for value in my_list:
    if type(value) == str:
        if value.isalpha():
                new_list.append(value)
print(f'4.', new_list)

################################# 5
my_str = 'Hello,mynameisDexterMorgan112'
new_list = [value for value in my_str if my_str.count(value) == 1]
print(f'5.', new_list)

################################# 6
my_str_1 = '132dexter1408www'
my_str_2 = 'dexter847lost13'
general_str = list(set(my_str_1) & set(my_str_2))
print(f'6.', general_str)

################################# 7
my_str_1 = '132dexter111408www2'
my_str_2 = 'dexter847lost113w0'
new_str_1 = [value for value in my_str_1.lower() if my_str_1.count(value) == 1]
new_str_2 = [value for value in my_str_2.lower() if my_str_2.count(value) == 1]
general_str = list(set(new_str_1) & set(new_str_2))
print(f'7.', general_str)

################################# 8
Проживание = {'Страна': 'Украина',
             'Город': 'Новомосковск',
             'Улица': 'Зины Белой'}
Работа = {'Наличие': True,
        'Должность': 'Специалист по снабжению сырьем и вспомогательными материалами' }

some_person = {"Фамилия": 'Тараненко',
               'Имя': 'Андрей',
               'Возраст': '27',
               'Проживание': Проживание,
               'Работа': Работа}

print(f'8. Характеристика:', some_person)

################################ 9

Коржи = {'Мука': '2,5 г.',
        'Молоко': '3,14 г.',
        'Масло': '200 г.',
        'Яйцо': '10 шт.',}
Крем = {'Сахар': '15 г.',
        'Масло': '25 г.',
        'Ваниль': '2,5 г.',
        'Сметана': '100 г.'}
Глазурь = {'Какао': '125 г.',
        'Сахар': '50 г.',
        'Масло': '25 г.'}

Составляющие = {'Коржи': Коржи,
    'Крем': Крем,
    'Глазурь': Глазурь}

amazing_biscuit = {'Составляющие': Составляющие}
print(f'9. Шикарный торт: ', amazing_biscuit)