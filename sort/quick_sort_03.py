'''
# shoter names of variables

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


def partition( a, start, end ):
    
    pi    = start
    pivot = a[ end ]

    for i in range( start, end ):

        if a[ i ] < pivot:
            # move to left
            a[ i ], a[ pi ] =  a[ pi ], a[ i ]
            pi += 1

    a[ pi ], a[ end ] =  a[ end ], a[ pi ]
    return pi


def quick_sort( a, start, end ):

    if start >= end:
        return

    pi = partition( a, start, end )
    quick_sort( a, start , pi - 1 )
    quick_sort( a, pi + 1, end    )

    return a


# ------------------------------------------------------
# Unit Test
# ------------------------------------------------------

data = random.sample( range( 0, 100 )  , 10 )
print( '\n\noriginal data: {}'.format( data ) )
s = quick_sort( data, 0, len( data )-1 )
print( 'sorted data: {} \n'.format( s ) )
