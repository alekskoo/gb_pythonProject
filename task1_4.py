n = int(input("Введите число: "))
max_digit = n % 10

while n > 0:
    n //= 10
    current_digit = n % 10
    if current_digit > max_digit:
        max_digit = current_digit

print(max_digit)

