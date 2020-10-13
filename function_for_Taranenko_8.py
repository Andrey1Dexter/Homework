import random
from random import randint, choice
############### 1 #############
def domains():
    with open('domains.txt'):
        domain_list = [line[1:-1] for line in open('domains.txt')]
        domain_list_1 = [random.choice(domain_list) for _ in range(1, len(domain_list)-1)]
        return domain_list_1

############### 2 #############
def names():
    names = open('names.txt', 'r')
    names_list = names.readlines()
    names_column_number = 1
    surname_list = []
    for surname in names_list:
        surname_list.append(surname.split()[names_column_number])
    names.close()
    return surname_list

############### 3 #############
import random
from random import randint, choice

def log_name():
    names = open('names.txt', 'r')
    names_list = names.readlines()
    names_column_number = 1
    surname_list = []
    for surname in names_list:
        surname_list.append(surname.split()[names_column_number])
    names.close()
    return surname_list[random.randint(1, len(surname_list)-1)]+'.'

def log_number():
    return randint(100, 999)
def log_letters():
    my_str = 'qwertyuioplkjhgfdsazxcvbnm'
    letters = [random.choice(my_str) for _ in range(randint(5, 7))]
    return '@' + ''.join(letters)
def log_domain():
    with open('domains.txt', 'r') as domain_list:
        domain = domain_list.readlines()[random.randint(1, 11)]
        return domain
def generate_email_list():
    return log_name() + str(log_number()) + log_letters() + str(log_domain())


