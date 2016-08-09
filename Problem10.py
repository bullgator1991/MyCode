import time

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


start_time = time.time()
total = 2
current = 3

while current < 2000000:
    total += (is_prime(current)*current)
    current += 2

print total

elapsed_time = time.time() - start_time

print str(elapsed_time) + ' seconds'