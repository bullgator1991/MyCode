import time
import math

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
#total = 2
current = 3
primes = 0

num = 600851475143
maxloop = 0
maxprimefactor = 0

maxloop = int(math.sqrt(num))

while current <= maxloop:
    if is_prime(current):
        if num % current == 0:
            maxprimefactor = current
    current += 2

print 'The max prime factor of ' + str(num) + ' is ' + str(maxprimefactor)

elapsed_time = time.time() - start_time

print str(elapsed_time) + ' seconds'