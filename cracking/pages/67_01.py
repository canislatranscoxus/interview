''''
description:    Findinf bottleneck.

                Given an array of distinct integer values, count the number of pairs of integers 
                that have difference k. For example, given the array

                { 1, 7, 5, 9, 2, 12, 3 } and the difference k = 2, 
                
                there aree four pairs with difference 2:

                (1, 3), (3, 5), (5, 7), (7, 9). 


First approach. This version use just one array. We sort the array and loop to search.

Time complexity:  O( n log n )

'''

def find_pairs( a, k ):
    size = len( a )
    a.sort()
    pairs = []

    for i in range( 0, size -1 ):
        for j in range( i + 1, size ):
            if a[ j ] == a[ i ] +k :
                print( '{}, {}'.format( a[i], a[j] ) )
                t = ( a[i], a[j] )
                pairs.append( t )
                break
            elif a[ j ] > a[ i ] +k :
                break
    
    return pairs

def ut_01():
    k           = 2
    a           = [ 1, 7, 5, 9, 2, 12, 3 ]
    expected    = [ (1, 3), (3, 5), (5, 7), (7, 9) ]
    pairs       = find_pairs( a, k )

    assert pairs == expected, 'Error in finding pairs'


if __name__ == '__main__':
    ut_01()
