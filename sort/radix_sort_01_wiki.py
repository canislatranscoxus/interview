'''
-------------------------------------------------------------------------------
Description : Radix Sort. Code adapted from website.

Author      : Arturo Alatriste Trujillo.

references  :
    https://en.wikipedia.org/wiki/Radix_sort
------------------------------------------------------------------------------- '''

import random


def list_to_buckets( array, base, iteration ):
    buckets = [[] for _ in range(base)]
    
    for number in array:
        # Isolate the base-digit from the number
        digit = (number // (base ** iteration)) % base
        
        # Drop the number into the correct bucket
        buckets[digit].append(number)

    return buckets

def buckets_to_list( buckets ):
    numbers = []
    
    for bucket in buckets:
        # append the numbers in a bucket
        # sequentially to the returned array
        for number in bucket:
            numbers.append(number)
    return numbers


def radix_sort( array, base = 10 ):

    maxval = max( array )
    it = 0

    # Iterate, sorting the array by each base-digit
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array

# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------


data =  random.sample( range( 100, 999 ), 10 )

print( '\n\n' )
print( 'original data: {0} '.format( data ) )

s = radix_sort( data )
print( 'sorted   data: {0}'.format( s ) )
print( '\n\n' )