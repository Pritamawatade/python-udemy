from functools import wraps
def logging_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before function calling "+func.__name__)
        result = func(*args, **kwargs)
        print("after function calling "+func.__name__)
        return result

    return wrapper

@logging_activity
def demo(type):
    print(f"chai = {type}")

demo("masala");
print(demo.__name__)
