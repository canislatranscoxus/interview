'''
-------------------------------------------------------------------------------
Description : Radix Sort using Counting sort, to sort the buckets.

Author      : Arturo Alatriste Trujillo.

references  :
    
    http://opendatastructures.org/ods-cpp/11_2_Counting_Sort_Radix_So.html
    https://en.wikipedia.org/wiki/Radix_sort
------------------------------------------------------------------------------- '''

import random


def get_key( number, position, base = 10 ):
    # number    : a positive integer
    # position  : the index of the digit from rigth to left that we want to extract
    # base      : base, by default is 10
    
    d = ( number // base ** position ) % 10
    return d



def radix_sort( array, base = 10 ):
    # array         : array or list with positive numbers to sort.
    # max_val       : the biggest value in input array.
    # i             : iteration counter
    # sorted_array  : the output, the sorted array.

    max_val  = max( array )
    position = 0


    #print( '\n\n Starting Radix sort with counting sort \n\n' )

    # Iterate, sorting the array by each base-digit
    while base ** position <= max_val:
        
        # we are doing Counting sort
        output = array.copy()
        count = [ 0 ] * (max_val + 1)

        # histogram
        for i in range( 0, len(array) ):
            j = get_key( output[ i ], position, base )
            count[ j ] = count[ j ] + 1

        # prefix sumatory
        for i in range( 1, len(count) ):
            count[ i ] = count[ i ] + count[ i - 1 ]

        # write output
        for i in range( len( array ) - 1, -1, -1 ):
            j = get_key( array[i], position, base )
            count[ j ] = count[ j ] - 1
            output[ count[ j ] ] = array[ i ]

        position += 1
        array     = output
        #print( 'output: {}'.format( output ) )

    return output

# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------


#data =  random.sample( range( 100, 999 ), 10 )

data = [ 3, 2, 6, 2, 1, 2, 3, 0, 2, 10 ]

print( '\n\n' )
print( 'original data: {0} '.format( data ) )

s = None
s = radix_sort( data )
print( 'sorted   data: {0}'.format( s ) )
print( '\n\n' )

'''
for i in range( 10 ):
    d = get_key( 9876543210, position= i, base = 10  )
    print( d )
'''

print( '\n ... end. \n' )    




