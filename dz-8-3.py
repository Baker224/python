def type_logger(func):
    def wrapper(args):
        print(f'{args}: {type(func(args))}')
        return func(args)

    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
