'''
---------------------------------------------------------------------------------------------------
Description : Radix Sort Algorithm. Taken from the book.

Author      : Arturo Alatriste Trujillo.

References  :
    Object Oriented C++ Data Structures for Real Programmers
    by Jan Harrington.
    Morgan Kaufmann.
--------------------------------------------------------------------------------------------------- '''



def radix( a ):
    '''

    :param a: array of data
    :return:
    '''
    total_elements = len( a )
    MAX_ELEMENTS   = total_elements
    dest_array     = [ 0 ] * total_elements
    sort_array     = a[:]
