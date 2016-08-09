import time
import math

def main():
    start_time = time.time()
    maxsum = 0
    maxa = 0
    maxb = 0
    for a in range (1,100,1):
        for b in range (1,100,1):
            num = str(a**b)
            #print num
            sumofdigits = 0
            numtostr = str(num)
            length = len(numtostr)
            for i in range(1, length+1):
                for z in range(i, i+1):
                    sumofdigits += int(numtostr[z-1:z])
            if sumofdigits > maxsum:
                maxsum = sumofdigits
                maxa = a
                maxb = b
                print 'maxsum is now ' + str(maxsum)
    elapsed_time = time.time() - start_time
    print "Sum of digits is %d" %(maxsum)
    print "a= " + str(maxa)
    print "b= " + str(maxb)
    print 'Elapsed time is: ' + str(elapsed_time) + ' seconds.'


main()