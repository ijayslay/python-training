# Handling Division Handling

try:
    x = 10/0

except ZeroDivisionError as e:
    print("Error:", e)
    b = 30
    print(b)

else:
    print("Division successful")
    print(x)

finally:
    print("Execution completed")
