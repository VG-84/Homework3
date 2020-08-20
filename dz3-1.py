# dz 3-1

def function(a: float, b: float) -> float:
    """ Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
    try:
        return a / b
    except ZeroDivisionError as e:
        print('Error 0')
    return None