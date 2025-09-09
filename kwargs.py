def show_info(**info):
    for key,value in info.items():
        print(key, value)
    


# Example 1: basic info
show_info(name="Jay", age=25, course="Python")

# Example 2: employee details
show_info(id=101, name="Aarav", department="IT", salary=55000)

# Example 3: book details
show_info(title="The Beast Eagle", author="Jay Patil", pages=320, genre="Fantasy")

# Example 4: car details
show_info(brand="Tesla", model="Model S", year=2024, color="Black")

# Example 5: student marks
show_info(name="Ari", maths=95, science=89, english=92)