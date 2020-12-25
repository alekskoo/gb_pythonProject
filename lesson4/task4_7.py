def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        print(factorial)
        factorial *= i
    yield factorial


for el in fact(12):
    print(el)
