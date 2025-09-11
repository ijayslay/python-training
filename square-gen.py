def square(n):
    for i in range (1,n+1):
        yield i*i

gen = square(5)

print(next(gen))        #1
print(next(gen))        #4
print(next(gen))        #9
print(next(gen))        #16
print(next(gen))        #25
