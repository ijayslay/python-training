thisset = {"apple", "banana", "cherry"}
print(thisset) 

for x in thisset:
  print(x) 

print("banana" in thisset) 
print("banana" not in thisset) 

thisset.add("orange")
print(thisset) 

thisset.remove("banana")    
print(thisset) 


thisset.discard("cherry")
print(thisset) 