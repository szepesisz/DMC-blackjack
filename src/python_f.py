
def task_1():
    """
    Alap operátorok
    """
    print(2 + 2 + 3)
    print(2 * 2 * 3)
    print(2 ** 2 ** 3)
    print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
    print(5 % 4, -5 % 4, -5 % -4)
    print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
    x = 0
    y = 10
    print(x < y and y % 2 == 0)


def task_2():
    """
    Bitszintű operátorok

    14 = 1*10 + 4*1
    14 = 1 * 10**1 + 4 * 10**0

    bin:   16 8 4 2 1
    14:     0 1 1 1 0  --> 1110
    6:      0 0 1 1 0  --> 110
    """

    print(bin(14))
    print(bin(6))
    print(bin(36))  # 100100
    print(bin(42))  # 101010

    print(36 & 42)
    print(bin(36 & 42))
    """
    AND (ÉS)
        100100
      & 101010
      --------
        100000
    """

    print(36 | 42)
    print(bin(36 | 42))
    """
    OR (VAGY)
        100100
      | 101010
      --------
        101110
    """
    print(36 ^ 42)
    print(bin(36 ^ 42))

    """
    XOR (KIZÁRÓ VAGY)
        100100
      ^ 101010
      --------
        001110
    """

    print(14 >> 1)
    """
    14: 1110
    7:   111
    """
    print(14 >> 2)
    """
    14: 1110
    7:   111(.0)
    3:    11(.1)
    """
    print(14 << 1)
    """
    14:  01110
    28:  11100
    """
    print(14 << 2)

def task_3():
    num = 1002
    if num % 2 == 0:
        print(f'A(z) {num} páros.')
    else:
        print(f'A(z) {num} páratlan.')

    if num & 1 == 0:
        print(f'A(z) {num} páros.')
    else:
        print(f'A(z) {num} páratlan.')

    """
    9: 1001
    1: 0001
    &: 0001
    
    8: 1000
    1: 0001
    &: 0000
    """

def task_4():
    """
    Egy szám 2 hatvány-e?

    2 hatvány   |   szám-1
      10000     |    1111
        100     |      11
    1000000     |  111111
    """
    a = 32
    if a & (a - 1) == 0:
        print(f'A(z) {a} 2-hatvány.')
    else:
        print(f'A(z) {a} nem 2-hatvány.')

def task_5():
    """
    Számrendszerek
    """
    num = 28
    con = 16
    if con == 2:
        converted_num = bin(num).replace('0b', '')
    if con == 8:
        converted_num = oct(num).replace('0o', '')
    if con == 16:
        converted_num = hex(num).replace('0x', '')
    print(converted_num)


def task_6():
    """
    Különböző számrendszerek
    """
    print(123 + 0b1011101 + 0o723 + 0x51da)


def task_7():
    a = 13
    b = 6
    print(f'a = {a} ({bin(a)})')
    print(f'b = {b} ({bin(b)})')

    print(f'{a} & {b} = {a & b} ({bin(a & b)})')


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    task_7()