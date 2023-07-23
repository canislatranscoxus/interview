'''
-------------------------------------------------------------------------------
Description: Quick Sort Algorithm. The algorithm was created by  Tony Hoare in 1959,
             and the code was adapted from the book.

author    : Arturo ALatriste Trujillo.

references:
    https://en.wikipedia.org/wiki/Quicksort

    Estructura de datos Tapa blanda – 1 ago 1998
    de Joyanes Aguilar (Autor),‎ Zahonero Martinez (Autor)
------------------------------------------------------------------------------- '''

import random

def swap( a, i, j ):
    '''
    In the array swap the values of elements from index i and j
    :param a: array of elements
    :param i: index i
    :param j: index j
    :return:
    '''
    tmp = a[ i ]
    a[ i ] = a[ j ]
    a[ j ] = tmp

def partition( a, first, last ):
    '''
    This is the recursive part of the algorithm.
    Create a pivot,
    move to the left  array elements less     than pivot, and
    move to the rigth array elements greather than pivot,
    then call recursively to sort left and right arrays.
    :param a    : array of data
    :param first: index of first element in the a array
    :param last : index of last  element in the a array
    :return: a is sorted
    '''
    i     = first
    j     = last
    p     = int( (first + last) / 2 )
    pivot = a[ p ]

    while True:
        while a[i] < pivot:
            i = i + 1

        while a[j] > pivot:
            j = j - 1

        if i <= j:
            swap( a, i, j)
            i = i + 1
            j = j - 1

        if i > j:
            break

    if first < j:
        partition( a, first, j )

    if i < last:
        partition( a, i, last  )



def quick_sort( a ):
    '''
    Code for Quick Sort Algorithm.
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
print( 'sorted   data: {0}'.format( data ) )
