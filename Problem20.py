import time
import math

def main():
    start_time = time.time()
    num = str(math.factorial(100))
    print num
    sumofdigits = 0
    numtostr = str(num)
    length = len(numtostr)
    for i in range(1, length+1):
        for z in range(i, i+1):
            sumofdigits += int(numtostr[z-1:z])

    elapsed_time = time.time() - start_time
    print "Sum of digits is %d" %(sumofdigits)
    print 'Elapsed time is: ' + str(elapsed_time) + ' seconds.'


main()