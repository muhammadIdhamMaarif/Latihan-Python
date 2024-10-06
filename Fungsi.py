import math

def luas_lingkaran(radius):
    return math.pi * radius ** 2

def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gabung_list(list1, list2):
    return list1 + list2
