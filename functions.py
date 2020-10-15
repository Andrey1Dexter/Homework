import random
from random import randint

def get_rand_0_255(mask_x):
    if mask_x <= 1:
        min = 0
        max = 9
    elif mask_x == 2:
        min = 10
        max = 99
    else:
        min = 100
        max = 255

    return str(randint(min, max))

def get_ip(mask = 'xx.x.xxx.xx'):
    ip_parts = [str(get_rand_0_255(len(some))) for some in mask.split('.')]
    return ".".join(ip_parts)

def sort_ip_key(ip):
    ip_parts = ip.split('.')
    # print('=======', ip_parts)
    key_list = []
    for part in ip_parts:
        # print('----->', part)
        key_list.append(int(part))
    # print(key_list)
    return key_list
############### OR ###########
    # return [int(part) for part in ip.split('.')]



def generate_list_ip_address(number: int, repeat=True, sort=False, mask = 'xx.x.xxx.xx') -> list:
    ip_list = []
    for _ in range(number):
        ip_list.append(get_ip())
    if not repeat:
        ip_list = list(set(ip_list))
    if sort:
        ip_list.sort(key=sort_ip_key)
    return ip_list


