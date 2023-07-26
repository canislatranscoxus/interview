'''
-----------------------------------------------------------------------------
description   : The original merge sort algorithm
                created by  1945 por John Von Neumann in 1945.

program author: Arturo Alatriste Trujillo.

references    :
    https://en.wikipedia.org/wiki/Merge_sort


    
    Data Structures & Algorithms in Python: Implementing Sorting Algorithms
    Kyshan Iyer
    https://acm.percipio.com/courses/5a3629ef-ec15-4314-beab-6ec49fc4094f/videos/54e3b10b-c303-4cf2-aaf9-ef9d82956146?tab=overview
    code
    https://acm.percipio.com/courses/5a3629ef-ec15-4314-beab-6ec49fc4094f/videos/54e3b10b-c303-4cf2-aaf9-ef9d82956146?id=afd82da0-c691-4d9f-bfe1-0dbe5d581f6a&tab=resources

    
-----------------------------------------------------------------------------
'''
import random


def do_merge( a, left, right ):

    i = 0
    j = 0
    k = 0

    while j < len( left ) and k < len( right ):
        if left[ j ] < right[ k ]:
            a[ i ] = left[ j ]
            j += 1
        else:
            a[ i ] = right[ k ]
            k += 1
        i += 1
    
    # add remaining elements from left
    while j < len( left ):
        a[ i ] = left[ j ]
        j += 1
        i += 1

    # add remaining elements from right
    while k < len( right ):
        a[ i ] = right[ k ]
        k += 1
        i += 1




def merge_sort( a ):
    if len( a ) <= 1:
        return 

    p = len( a ) // 2
    left  = a[  : p ]
    right = a[ p:   ]

    merge_sort( left  )
    merge_sort( right )
    do_merge( a, left, right )

    return a



# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------

data =  random.sample( range( 1, 100 ), 10 )
n = len( data )
print( '\n\n original data: {0} '.format( data ) )

s = merge_sort( data )
print( 'sorted data: {0} \n'.format( data ) )
