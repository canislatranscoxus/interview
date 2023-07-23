'''
Description: Quick Sort Algorithm.

author    : Arturo ALatriste Trujillo.
references:

    Estructura de datos Tapa blanda – 1 ago 1998
    de Joyanes Aguilar (Autor),‎ Zahonero Martinez (Autor)

'''

import random

def swap( a, i, j ):
    '''
    In the array a swap the values of elements from index i and j
    :param a: array of elements
    :param i: index i
    :param j: index j
    :return:
    '''
    tmp = a[ i ]
    a[ i ] = a[ j ]
    a[ j ] = tmp

def partition( a, first, last ):


    i     = first
    j     = last
    p     = int( (first + last) / 2 )
    pivot = a[ p ]

    #print( 'first: {0}'.format( first ) )
    #print( 'last : {0}'.format( last  ) )
    #print( 'i    : {0}'.format( i     ) )
    #print( 'j    : {0}'.format( j     ) )
    #print( 'p    : {0}'.format( p     ) )
    #print( 'pivot: {0}'.format( pivot ) )

    #print( ' a: {0}'.format( a ) )


    while True:
        while a[i] < pivot:
            i = i + 1

        while a[j] > pivot:
            j = j - 1

        if i <= j:
            swap( a, i, j)
            i = i + 1
            j = j - 1
            #print( a )

        if i > j:
            break


    #print( 'swapped: {0}'.format( a ) )


    if first < j:
        #print( 'left: {0}'.format( a[ first: j ] ) )
        partition( a, first, j )

    if i < last:
        #print( 'right: {0}'.format( a[ i: last ] ) )
        partition( a, i, last  )



def quick_sort( a ):
    '''

    :param a: array with numbers

    :return:
    '''
    num_elements = len( a )
    partition( a, 0, num_elements - 1 )

# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------


data =  random.sample( range( 1, 100 ), 10 )
n = len( data )
print( 'original data: {0} '.format( data ) )

s = quick_sort( data )
print( 'sorted data: {0}'.format( data ) )
