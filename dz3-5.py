# dz3-5

def sum(*args):
    res = 0
    ex = False
    for itm in args:
        try:
            res +=float(itm) if itm else  0
        except ValueError as e:
            if itm == 'q':
                ex = not ex
                break
    return res, ex

sum_1 = 0
while True:
    hello_1 = input('Введи числа\n').split(' ')
    user_sum, user_exit = insert_sum(*hello_1)
    sum_1 += user_sum
    print(f'total: {sum_1}')

    if user_exit:
        print('See you latter')
        break