import time
def timer(func): # this will contain the name of the function name
    def wrapper(args_for_function): # this will contain the arguments of the function
        start = time.time()
        func(args_for_function)
        end = time.time()
        print('func takes', end - start, 'seconds')

    return wrapper  # this will return the wrapper function


@timer  # call the decorator function
def func1(args_for_function):
    ...  # something happens here