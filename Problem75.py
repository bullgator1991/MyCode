import time

start_time = time.time()

for l in range(12, 1500, 2):

    for a in range(int(.25*l), int(.4*l), 1):
        for b in range(int(a), int(2.5*a), 1):
            for c in range(b+1, l-(a+b)+1, 1): #(a < b < c)
                if ((a**2 + b**2) == c**2) and (a+b+c == l):
                    elapsed_time = time.time() - start_time
                    print 'a= ' + str(a) + ', b= ' + str(b) + ', c= ' + str(c)
                    print 'Product of a*b*c is: ' + str(a*b*c)
                    print '"Length is: ' + str(l)
                    print 'Elapsed time is: ' + str(elapsed_time) + ' seconds.'




