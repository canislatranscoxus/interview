'''
page: 90

interview Question: 

1.1 Determine an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures ?

    strategy: use  a dictionary. We can handle for unicode symbols. there are 2^32 symbols.


Complexity:  O( n )

where n is the size of the string


→ ⟹ ￫ ≈
'''


def has_unique_chars( s ):
    d = dict() 

    for ch in s:

        if ch in d:
            print( 'we found duplicated the char: {}'.format( ch ) )
            return False
        else:
            d[ ch ] = 1


    return True

def ut1( ):
    s = 'abcdef'
    print( '\n\n string: {}'.format( s ) )
    if has_unique_chars( s ):
        print( 'This string has unique chars' )
    else:
        print( 'This string has duplicated chars' )

def ut2( ):
    s = 'anim@ls from_the-juNgLE'
    print( '\n\n string: {}'.format( s ) )
    if has_unique_chars( s ):
        print( 'This string has unique chars' )
    else:
        print( 'This string has duplicated chars' )



# -----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    ut1()
    ut2()
    print( '... end. \n')