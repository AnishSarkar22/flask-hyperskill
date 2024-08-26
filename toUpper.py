# convert to upper case using decorator function
# *args captures all positional arguments
# **kwargs captures all keyword arguments.

def to_upper(func):
    def wrapper(*args, **kwargs): 
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@to_upper
def say_hello():
    return "I love Python!"