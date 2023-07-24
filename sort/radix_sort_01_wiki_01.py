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
        buckets[ digit ].append( number )

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
    # array         : array or list with positive numbers to sort.
    # max_val       : the biggest value in input array.
    # i             : iteration counter
    # sorted_array  : the output, the sorted array.

    max_val = max( array )
    i = 0

    sorted_array = array

    # Iterate, sorting the array by each base-digit
    while base ** i <= max_val:
        sorted_array = buckets_to_list( list_to_buckets( sorted_array, base, i ) )
        i += 1

    return sorted_array

# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------


#data =  random.sample( range( 100, 999 ), 10 )

data = [ 678, 34, 112, 9, 824, 5, 16, 123, 30, 1  ]

print( '\n\n' )
print( 'original data: {0} '.format( data ) )

s = radix_sort( data )
print( 'sorted   data: {0}'.format( s ) )
print( '\n\n' )