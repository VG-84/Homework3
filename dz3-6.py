# dz3-6

def user_functions(string: str):
    return ' '.join((string[0].upper(), string[1:])) if string else  string
def user_data(string: str):
    return ' '.join(map(user_functions, string.split(' ')))