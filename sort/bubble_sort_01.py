'''
---------------------------------------------------------------------------------------------------

Description: Bubble sort.

Author: Arturo Alatriste Trujillo.

references:
    https://www.topcoder.com/community/data-science/data-science-tutorials/sorting/
--------------------------------------------------------------------------------------------------- '''
import random

def bubble_sort( a ):
    print( 'bubble_sort working ...' )
    n = len( a )
    for i in range( 0, n -1 ):
        for j in range( 0, n -1 ):
            if a[ j ] > a[ j + 1]:
                swap       = a[ j     ]
                a[ j     ] = a[ j + 1 ]
                a[ j + 1 ] = swap

# -------------------------------------------------------------------------------------------------



data =  random.sample( range( 1, 100 ), 10 )

print( 'original data: {0} '.format( data ) )

s = bubble_sort( data )
print( 'sorted data: {0}'.format( data ) )