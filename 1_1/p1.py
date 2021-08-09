'''
page: 90

interview Question: 

1.1 Determine an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures ?

    strategy: we use a list. We are using a data structure.


Complexity:  O( n log n )

(n log n) + n
because we sort, then loop.

'''

def has_unique_chars( s ):
    a = list( s )
    a.sort()
    size = len( a )

    for i in range( 0, size - 1 ):
        if a[ i ] == a[ i + 1 ]:
            print( 'we found duplicated the char: {}'.format( a[i] ) )
            return False

    return True


s = 'abcdef'
if has_unique_chars( s ):
    print( '"{}", has unique chars'.format( s ) )
else:
    print( '{}, has duplicated chars'.format( s ) )