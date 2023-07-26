'''
This script was done based on the next course

acm. percipio

Data Structures & Algorithms in Python: Implementing Sorting Algorithms.
Chapter: Coding the Quick sort algorithm.
Kishan Iyer

links:

course
https://acm.percipio.com/courses/5a3629ef-ec15-4314-beab-6ec49fc4094f/videos/54e3b10b-c303-4cf2-aaf9-ef9d82956146?tab=overview


code
https://acm.percipio.com/courses/5a3629ef-ec15-4314-beab-6ec49fc4094f/videos/54e3b10b-c303-4cf2-aaf9-ef9d82956146?id=7bddce52-7abd-4716-b759-ba107cebb367&tab=resources

'''
import random

def swap( array, i, j ):
    tmp =  array[ i ]
    array[ i ] = array[ j ]
    array[ j ] = tmp


def partition( array, start_idx, end_idx ):
    
    pivot_idx = start_idx
    pivot     = array[ end_idx ]

    for i in range( start_idx, end_idx ):

        if array[ i ] < pivot:
            # move to left
            array[ i ], array[ pivot_idx ] =  array[ pivot_idx ], array[ i ]
            pivot_idx += 1

    array[ pivot_idx ], array[ end_idx ] =  array[ end_idx ], array[ pivot_idx ]
    return pivot_idx


def quick_sort( array, start_idx, end_idx ):

    if start_idx >= end_idx:
        return

    pivot_idx = partition( array, start_idx, end_idx )
    quick_sort( array, start_idx    , pivot_idx - 1 )
    quick_sort( array, pivot_idx + 1, end_idx       )

    return array


# ------------------------------------------------------
# Unit Test
# ------------------------------------------------------

data = random.sample( range( 0, 100 )  , 10 )
print( '\n\noriginal data: {}'.format( data ) )
s = quick_sort( data, 0, len( data )-1 )
print( 'sorted data: {} \n'.format( s ) )
