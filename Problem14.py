
import math

longestchain = 0
longestchainstarter = 0
chain = 1


current = 13
while current < 1000000:
    sequence = current
    while sequence <> 1:
        if sequence % 2 == 0:
            sequence = (sequence/2)
        else:
            sequence = (sequence*3)+1
        chain += 1
        #print sequence

    if chain > longestchain:
        longestchain = chain
        longestchainstarter = current
    #print 'Current was: ' + str(current)
    current += 1
    chain = 1

print longestchain
print longestchainstarter
