# The sum of the squares of the first ten natural numbers is,
# 1^(2) + 2^(2) + ... + 10^(2) = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^(2) = 55^(2) = 3025

# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 3025
# - 385 = 2640.

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

# using sum of squares and square of sum of natural nos, 

n = 100
result = ( n*(n+1)/2 )**2 - n*(n+1)*(2*n+1)/6
print result

