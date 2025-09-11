
def my_deco(say_hello):
    def wrapper():
        print("before calling hello")
        say_hello()
        print("after calling hello")
    return wrapper

def second_deco(func):
    def wrapper():
        print("==Extra Functionality")
        func()
        print("==End of Extra")
    return wrapper
@my_deco
@second_deco

def func():
    print("Welcome habibi")
func() 

def say_hello():        #original code for function
    print("Hello Team")
say_hello()

