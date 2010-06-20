# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143

import sys

n = 600851475143 

def is_prime( num ):
    for i in range( 2 , num ** 0,5 ):
        if n % i == 0:
            return False

    return True

powers = {}
i = 2

while n != 1 : 
    if is_prime( i ):
        if n % i == 0:
            try:
                powers[i] += 1
            except:
                powers[i] = 1
            n /= i
        else:
            i += 1
    else:
        i += 1
        
print ( max( powers.keys() ) )
