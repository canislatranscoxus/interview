'''
---------------------------------------------------------------------------------------------------

Description: Optimized Bubble sort, this algorithm does not search at the sorted elements
             in the inner loop. This code is based on the book.


Author: Arturo Alatriste Trujillo.

references:
    https://en.wikipedia.org/wiki/Bubble_sort

    Object Oriented C++ Data Structures for Real Programmers
    Jan Harrington.
    Morgan Kaufmann.
--------------------------------------------------------------------------------------------------- '''
import random

def bubble_sort( a ):
    print( 'bubble_sort working ...' )
    n              = len( a )
    swapped        = True
    unsorted_index = n - 1
    tmp_index      = 0

    while swapped:
        swapped = False
        for i in range( 0, unsorted_index ):
            if a[ i ] > a[ i + 1]:
                swapped    = True
                swap       = a[ i     ]
                a[ i     ] = a[ i + 1 ]
                a[ i + 1 ] = swap
                tmp_index  = i

        unsorted_index = tmp_index


# -------------------------------------------------------------------------------------------------



data =  random.sample( range( 1, 100 ), 10 )

print( 'original data: {0} '.format( data ) )

s = bubble_sort( data )
print( 'sorted data: {0}'.format( data ) )