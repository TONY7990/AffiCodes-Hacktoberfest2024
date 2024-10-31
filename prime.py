def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_numbers_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input
n = int(input("Find prime numbers up to: "))
primes = prime_numbers_up_to(n)
print(f"Prime numbers up to {n}: {primes}")
