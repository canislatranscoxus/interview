'''
-------------------------------------------------------------------------------
Description : Radix Sort. Code adapted from website.

Author      : Arturo Alatriste Trujillo.

references  :
    https://en.wikipedia.org/wiki/Radix_sort
------------------------------------------------------------------------------- '''

import random


def list_to_buckets( a, base, exp ):
    
    buckets = [[] for _ in range(base)]
    divisor = base ** exp

    for number in a:
        # Isolate the base-digit from the number. The bucket index.
        digit = ( number // divisor ) % base
        
        # Drop the number into the correct bucket
        buckets[ digit ].append( number )

    return buckets


def buckets_to_list( buckets ):
    # append the numbers from the buckets sequentially in an array.
    a = []
    
    for bucket in buckets:
        for number in bucket:
            a.append( number )
    return a


def radix_sort( a, base = 10 ):
    # a             : array or list with positive numbers to sort.
    # max_val       : the biggest value in input array.
    # i             : iteration counter

    max_val = max( a )
    exp = 0

    # Iterate, sorting the array by each base-digit
    while base ** exp <= max_val:
        a    = buckets_to_list( list_to_buckets( a, base, exp ) )
        exp += 1
    return a

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