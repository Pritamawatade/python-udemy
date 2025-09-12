from functools import wraps
def my_decorator(func):

     # it preserve the name of the function
    def wrapper():
        print("before the function runs "+ func.__name__)
        func()
        print("after the function runs "+ func.__name__)
    return wrapper


@my_decorator
def gree():
    print("hello from decorator")

gree()
print(gree.__name__)