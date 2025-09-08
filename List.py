a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)

print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3

a = []

a.append(10)  
print("After append(10):", a)  

a.insert(0, 5)
print("After insert(0, 5):", a) 

a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 

print(a)

a.clear()
print("After clear():", a)

#next Problem
a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

pop_val = a.pop(1)  
print("Popped element:", pop_val)
print("After pop(1):", a) 

#delete elemet
del a[0]  
print("After del a[0]:", a)
