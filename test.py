import math
number = int(input("Enter a number to check if it's prime: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def list_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

api_key = "12345-abcdef-67890"

try:
    divisor = int(input("Enter a divisor for calculation: "))
    result = 100 / divisor
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

unused_variable = "This is not used anywhere"