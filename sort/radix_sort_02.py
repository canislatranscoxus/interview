'''
-------------------------------------------------------------------------------
Description: Radix Sort Algorithm. The code was adapted from the book.
Not Working.

Author     : Arturo Alatriste Trujillo.

references :
    Mastering Algorithms with C
    by Kyle Loudon
    Publisher: O'Reilly Media, Inc.
    Release Date: August 1999
    ISBN: 9781565924536

    https://en.wikipedia.org/wiki/Radix_sort

------------------------------------------------------------------------------- '''

import math
import random
# -------------------------------------------------------------------------------                                                                            *
#                                  rxsort
# -------------------------------------------------------------------------------

def rxsort( data, p, k = 10):
    '''

    :param data: the array with data
    :param p   : specifies the number of digit positions in each integer.
    :param k   : the radix. For integers we use 10 by default.
    :return    : data array is sorted.
    '''
    size = len( data )

    # buckets count array
    counts = [0] * k

    # sorted elements array
    temp   = [0] * size

    index  = 0
    pval   = 0
    i      = 0
    j      = 0
    n      = 0

    # -------------------------------------------------------------------------------
    #  Sort from the least significant position to the most significant.         *
    # -------------------------------------------------------------------------------
    for n in range( 0, p ):
        #  Initialize the counts.                                                 *
        for i in range( 0, k ):
              counts[ i ] = 0

        #  Calculate the position value.                                          *
        pval = pow( k, n)

        #  Count the occurrences of each digit value.                             *
        for j in range( 0, size ):
              index           = int( data[j] / pval ) % k
              counts[ index ] = counts[ index ] + 1

        #  Adjust each count to reflect the counts before it.                     *
        for i in range( 1, k ):
              counts[ i ]     = counts[ i ] + counts[ i - 1 ]

        #  Use the counts to position each element where it belongs.              *
        for j in range( size - 1, -1, -1 ):
            index                      = int(data[ j ] / pval) % k
            temp[ counts[ index ] - 1] = data[ j ]
            counts[ index ]            = counts[ index ] - 1

        #  Prepare to pass back the data as sorted thus far.                      *
        for j in range( 0, size):
            data[ j ] = temp[ j ]

    # -------------------------------------------------------------------------------
    #  Free the storage allocated for sorting.                                   *
    # -------------------------------------------------------------------------------
    counts.clear()
    temp.clear()
    counts = None
    temp   = None

# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------

data =  random.sample( range( 100, 999 ), 10 )
p    = 3
print( 'original data: {0} '.format( data ) )

rxsort( data, p )
print( 'sorted   data: {0}'.format( data ) )
