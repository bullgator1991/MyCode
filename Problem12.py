
import time

def countFactors(n):
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

start_time = time.time()
done = False
currentTriangleNumber = 1
counter = 1

while done == False:
    if countFactors(currentTriangleNumber) > 500:
        done = True
        print currentTriangleNumber
    else:
        counter += 1
        currentTriangleNumber = currentTriangleNumber + counter

elapsed_time = time.time() - start_time

print str(elapsed_time) + ' seconds'



