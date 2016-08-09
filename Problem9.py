import time

start_time = time.time()

for a in range(1,201,1):
    for b in range (a,401,1):
        for c in range (b,501,1):
            if (a < b < c) and ((a**2 + b**2) == c**2) and (a+b+c == 1000):
                elapsed_time = time.time() - start_time
                print 'a= ' + str(a) + ', b= ' + str(b) + ', c= ' + str(c)
                print 'Product of a*b*c is: ' + str(a*b*c)
                print 'Elapsed time is: ' + str(elapsed_time) + ' seconds.'




