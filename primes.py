limit = int(input("Enter the limit: "))

print("Prime numbers:")
print("Prime numbers latest:")

for num in range(2, limit + 1):

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")