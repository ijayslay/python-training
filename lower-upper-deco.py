def to_uppercase(func):
    def wrapper():
        result = func()         
        return result.upper()   
    return wrapper

@to_uppercase

def func():
    return "hello world"

print(func())   
