def odd_numbers(n):
    for i in range(1, n+1):
        if i % 2 != 0:   # check odd
            yield i


gen = odd_numbers(10)

print(next(gen))  # 1
print(next(gen))  # 3
print(next(gen))  # 5
print(next(gen))  # 7
print(next(gen))  # 9