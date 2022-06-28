# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned {result}")
    
    return wrapper_function

@logging_decorator
def add(*args):
    return sum(args)
    
# Use the decorator 👇
              
add(2, 3, 5, 8, 9)
