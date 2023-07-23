'''
-----------------------------------------------------------------------------
description   : The original merge sort algorithm
                created by  1945 por John Von Neumann in 1945.

program author: Arturo Alatriste Trujillo.

references    :
    https://en.wikipedia.org/wiki/Merge_sort
-----------------------------------------------------------------------------
'''
import random

def do_merge( a, first, middle, last ):
    '''

    :param a     : array with data
    :param first : starting index of the first array
    :param middle: starting index of the second array
    :param last  : the index of the last element of the array
    :return      : array a will be sorted
    '''
    # create auxiliary array
    num_elements = len( a )
    aux          = [ 0 ] * num_elements

    first_ind    = first
    middle_ind   = middle + 1
    aux_ind      = first

    # oop to merge sorted arrays
    while first_ind <= middle and middle_ind <= last :
        if a[ first_ind ] <= a[ middle_ind ]:
            aux[ aux_ind ] = a[ first_ind  ]
            first_ind      = first_ind + 1
        else:
            aux[ aux_ind ] = a[ middle_ind ]
            middle_ind     = middle_ind + 1

        aux_ind = aux_ind + 1

    # loop to copy remaining elements.'
    while first_ind <= middle:
        aux[ aux_ind ] = a[ first_ind ]
        first_ind      = first_ind + 1
        aux_ind        = aux_ind   + 1

    while middle_ind <= last:
        aux[ aux_ind ] = a[ middle_ind]
        middle_ind     = middle_ind + 1
        aux_ind        = aux_ind    + 1

    # copy aux to list
    for i in range( first, last  ):
        a[ i ] = aux[ i ]


def merge_sort( a, first, last ):
    '''
        Split the array in two arrays.
        Sort the arrays
        merge the sorted arrays.
    :param a    : array os data
    :param first: the starting index.
    :param last : the ending index
    :return     : a sorted array.
    '''
    if first < last:
        middle = int( ( first + last ) / 2  )
        merge_sort(a, first , middle )
        merge_sort(a, middle + 1, last   )
        do_merge( a, first, middle, last )

# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------

data =  random.sample( range( 1, 100 ), 10 )
n = len( data )
print( 'original data: {0} '.format( data ) )

s = merge_sort( data, 0, n-1 )
print( 'sorted data: {0}'.format( data ) )
