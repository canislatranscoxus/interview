'''
page: 90

interview Question: 

1.1 Determine an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures ?

    strategy: we loop the string.

Complexity:  O( n^2 )

n * n/2 = (n^2) / 2 => n^2

'''

def has_unique_chars( s ):
    size = len( s )

    for i in range( 0, size - 1 ):
        for j in range( i+1, size ):
            if s[ i ] == s[ j ]:
                print( 'we found duplicated the char: {}'.format( s[i] ) )
                return False

    return True


#s = 'abcdef'
s = 'anim@ls from_the-juNgLE'
if has_unique_chars( s ):
    print( '"{}", has unique chars'.format( s ) )
else:
    print( '{}, has duplicated chars'.format( s ) )