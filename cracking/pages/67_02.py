''''
description:    Findinf bottleneck.

                Given an array of distinct integer values, count the number of pairs of integers 
                that have difference k. For example, given the array

                { 1, 7, 5, 9, 2, 12, 3 } and the difference k = 2, 
                
                there aree four pairs with difference 2:

                (1, 3), (3, 5), (5, 7), (7, 9). 


Second approach. move the data from array to dictionary. Then loop once the dictionary.

Time complexity:  using simple dictionary is O( n )
                    using OrderedDict for testing purposes, we sort keys, so 
                    time complexity is O( n log n )

'''

from collections import OrderedDict

def find_pairs( a, k ):
    '''
    a = array of numbers
    k = difference
    x = an number in the array
    d = a dictionary with the numbers. Used to search faster.
    '''
    size    = len(a)
    d       = OrderedDict()
    pairs   = []
    for i in range( 0, size):
        x = a[ i ]
        if x in d:
            d[ x ] = d[ x ] + 1
        else:
            d[ x ] = 1

    d.sorted_keys = lambda : sorted( d.keys() )
    for x in d.sorted_keys():
        if x + k in d:
            pair = ( x, x + k )
            pairs.append( pair )
            print( '{}'.format( pair ) )

    return pairs

def ut_01():
    k             = 2
    a             = [ 1, 7, 5, 9, 2, 12, 3 ]
    expected      = [ (1, 3), (3, 5), (5, 7), (7, 9) ]
    pairs         = find_pairs( a, k )
    assert pairs == expected, 'Error in finding pairs'



if __name__ == '__main__':
    ut_01()


