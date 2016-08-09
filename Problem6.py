
# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum
# three thousand twenty five minus three eighty five equals 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



x = 1
sumOfSquares = 0

while x <= 100:
    sumOfSquares += x* x
    x += 1

print sumOfSquares

x = 1
squareOfSums = 0
sums = 0

while x <= 100:
    sums += x
    x += 1

squareOfSums = sums * sums

print squareOfSums

print squareOfSums - sumOfSquares

