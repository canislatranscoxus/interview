'''
---------------------------------------------------------------------------------------------------

Description: A better Bubble sort, this algorithm does not search at the end of the list
             in the inner loop.

Author: Arturo Alatriste Trujillo.

references:
    https://www.topcoder.com/community/data-science/data-science-tutorials/sorting/
--------------------------------------------------------------------------------------------------- '''
import random

def bubble_sort( a ):
    print( 'bubble_sort working ...' )
    n = len( a )
    swapped = True

    while swapped:
        swapped = False
        for i in range( 0, n -1 ):
            if a[ i ] > a[ i + 1]:
                swap       = a[ i     ]
                a[ i     ] = a[ i + 1 ]
                a[ i + 1 ] = swap
                swapped    = True


# -------------------------------------------------------------------------------------------------



data =  random.sample( range( 1, 100 ), 10 )

print( 'original data: {0} '.format( data ) )

s = bubble_sort( data )
print( 'sorted data: {0}'.format( data ) )