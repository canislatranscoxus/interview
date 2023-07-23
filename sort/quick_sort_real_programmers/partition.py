'''
---------------------------------------------------------------------------------------------------
Description : Non Recursive Quick Sort Algorithm. Taken from the book.

Author      : Arturo Alatriste Trujillo.

References  :
    Object Oriented C++ Data Structures for Real Programmers
    Jan Harrington.
    Morgan Kaufmann.
--------------------------------------------------------------------------------------------------- '''

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


def partition( a, low, high ):
    pivot_point = low
    pivot_key   = a[ pivot_point ]

    while low <= high:
        if a[ low ] <= pivot_key:
            low = low + 1
        elif a[ high ] >= pivot_key:
            high = high - 1
        else:
            swap( a, low, high )
            low  = low  + 1
            high = high - 1

    swap( a, pivot_point, high )

    # this is is the spot between the two partitions
    pivot_point = high

    return pivot_point


