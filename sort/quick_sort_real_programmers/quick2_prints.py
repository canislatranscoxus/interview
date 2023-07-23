'''
---------------------------------------------------------------------------------------------------
Description : Non Recursive Quick Sort Algorithm. Taken from the book.

Author      : Arturo Alatriste Trujillo.

References  :
    Object Oriented C++ Data Structures for Real Programmers
    by Jan Harrington.
    Morgan Kaufmann.
--------------------------------------------------------------------------------------------------- '''
from partition import partition
import random

def quick2( a ):
    '''

    :param a:
    :return:
    '''
    total_elements = len( a )
    STACK_SIZE     = total_elements

    low            = 0
    high           = total_elements - 1

    pivot_point    = 0
    stack_ptr      = -1
    low_stack      = [ 0 ] * STACK_SIZE
    high_stack     = [ 0 ] * STACK_SIZE
    pass_count     = 1

    while True:

        # is non empty stack? set indexes
        if ( stack_ptr > -1 ):
            low       = low_stack [ stack_ptr ]
            high      = high_stack[ stack_ptr ]
            stack_ptr = stack_ptr - 1

        while low < high:
            print( 'a, before partition: {0}'.format(a))
            print( 'low : {0}'.format( low  ) )
            print( 'high: {0}'.format( high ) )
            print( 'pivot_point: {0}'.format( pivot_point ) )


            pivot_point = partition( a, low, high )

            if pivot_point - low < high - pivot_point:
                if stack_ptr >= STACK_SIZE:
                    print( 'Stack overflow. Cannot complete sort' )
                    return
                stack_ptr               = stack_ptr   + 1
                low_stack [ stack_ptr ] = pivot_point + 1
                high_stack[ stack_ptr ] = high
                high                    = pivot_point - 1
            else:
                if stack_ptr >= STACK_SIZE:
                    print('Stack overflow. Cannot complete sort')
                    return
                stack_ptr               = stack_ptr   + 1
                low_stack [ stack_ptr ] = low
                high_stack[ stack_ptr ] = pivot_point - 1
                low                     = pivot_point - 1
                pass_count              = pass_count  + 1

            print( 'pass #: {0}'.format( pass_count ) )
            print( 'low_stack : {0}'.format( low_stack  ) )
            print( 'high_stack: {0}'.format( high_stack ) )
            print( 'a: {0}'.format( a ) )

        # is empty stack? break
        if stack_ptr <= -1:
            break



# -----------------------------------------------------------------------------
# test
# -----------------------------------------------------------------------------

data =  random.sample( range( 1, 100 ), 10 )
n = len( data )
print( 'original data: {0} '.format( data ) )

s = quick2( data )
print( 'sorted   data: {0}'.format( data ) )
