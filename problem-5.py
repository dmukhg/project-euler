# 2520 is the smallest number that can be divided by each of 
# the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

import math
''' My algorithm:

    multiply all the highest powers of primes
'''

n = 20

def prime_( num ):
    for fac in range( 2, num ):
        if num % fac == 0:
            return False
    return True

prime_list = [ _ for _ in range( 2 , n+1 ) if prime_( _ ) ]

result = 1 

for prime in prime_list:
    result *= prime ** ( int( math.log( n , prime ) ) )

print result
