def login(func):
    def wrapper(user):
        if not user.get("is_logged_in"): #check login
            print("access denie! pls login")
            return None
        return func(user)
    return wrapper

@login

def dashboard(user):
    print("Welcome"+ user["name"]+"to your dashboard!")

## Test Cases
user1 = {"name": "Ghost","is_logged_in": True}
user2 = {"name": "Guest","is_logged_in":False}

dashboard(user1)
dashboard(user2)


