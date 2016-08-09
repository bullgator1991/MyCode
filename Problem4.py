
import numpy
import scipy


def is_palindrome(n):

    first, second, third, fourth, fifth, sixth = str(n)

    if first == sixth and second == fifth and third == fourth:
        return True

    return False

largestPalindrome = 0

for x in range(500, 999):
    for y in range(500, 999):
        current = x*y
        # print current
        if is_palindrome(current) and (current > largestPalindrome):
            largestPalindrome = current

print str(largestPalindrome) + ' is the largest palindrome of 3 digit numbers multiplied together. '

