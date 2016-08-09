
ands = 'and'
singles = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten = 'ten'
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decis = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
thousands = 'onethousand'



# do singles
total = 0
ones = 0
teen = 0
deci = 0
hundred = 0

currentstring = ''

# count single digit characters
for i in range (0,9,1):
    currentstring += singles[i]
    print singles[i]

print currentstring
print len(currentstring)

print ten
currentstring += ten
print currentstring
print len(currentstring)

# count teen characters
for i in range (0,9,1):
    currentstring += teens[i]
    print teens[i]

print currentstring
print len(currentstring)


# count decis
for i in range (0,8,1):
    print decis[i]
    currentstring += decis[i]
    for j in range (0,9,1):
        print decis[i] + ' ' + singles[j]
        currentstring += decis[i]
        currentstring += singles[j]

print currentstring


# count hundreds
for h in range (0, 9, 1):
        print hundreds[h]
        currentstring += hundreds[h]

        for s in range (0, 9, 1):
            print hundreds[h] + ' ' + ands + ' ' + singles[s]
            currentstring += hundreds[h] + ands + singles[s]

        print hundreds[h] + ' ' + ands + ' ' + ten
        currentstring += hundreds[h] + ands + ten

        for t in range (0,9,1):
            print hundreds[h] + ' ' + ands + ' ' + teens[t]
            currentstring += hundreds[h] + ands + teens[t]

        for i in range (0,8,1):
            print hundreds[h] + ' ' + ands + ' ' + decis[i]
            currentstring += hundreds[h] + ands + decis[i]
            for j in range (0,9,1):
                print hundreds[h] + ' ' + ands + ' ' + decis[i] + ' ' + singles[j]
                currentstring += hundreds[h] + ands + decis[i] + singles[j]

print thousands
currentstring += thousands

print currentstring
print len(currentstring)







          #  print hundreds[h] + ' ' + ands + ' ' + decis[i]
          #  for k in range(0, 9, 1):
          #      print hundreds[i] + ' ' + ands + ' ' + decis[j] + ' ' + singles[k]
          #      hundred += len(hundreds[i]) + len(decis[j]) + len(singles[k])

print len(singles)
print len(teens)
print len(decis)
print len(hundreds)
print len(thousands)
