def login(secret_page):
    def wrapper(username, password):
        cor_user = "root"
        cor_pass = "1111"
        
        if username == cor_user and password == cor_pass:
            print("Login Successful")
        else:
            print(" Login Failed! Invalid username or password")
    return wrapper

@login
def secret_page():
    print("Welcome to the Secret Page")

user = input("Enter username: ")
pwd = input("Enter password: ")

secret_page(user, pwd)
