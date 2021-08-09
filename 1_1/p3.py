'''
page: 90

interview Question: 

1.1 Determine an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures ?

    strategy: use array of bits. It takes very small space.
    If we use ascii (extended table) characters we can handle 256 symbols, 
    we need 256 bits, it is 32 bits, 4 bytes, the same as the size of an integer.
    
    If we use unicode, we need another strategy.

Complexity:  O( n )

O(1) + O(n) ⟹ O(n)  

create the bit array is always the same complexity, 
because the bit array always will have the same size

and loop the string.

→ ⟹ ￫ ≈
'''

class MyBitmap:
    a = None

    def get_bit( self, idx ):
        my_decimal = self.a & ( 1 << idx )
        return my_decimal

    def get_bit_normalized( self, idx ):
        my_bit = ( self.a >> idx )  & 1 
        return my_bit


    def set_bit( self, idx ):
        self.a = self.a | ( 1 << idx )

    def unset_bit( self, idx ):
        self.a = self.a & ~( 1 << idx )


    def __init__( self, size ):
        self.a = 1 << (size - 1)
        self.unset_bit( size - 1 )    



def has_unique_chars( s ):
    bitmap = MyBitmap( 256 ) # we are using ascci extended table

    for ch in s:
        i = ord( ch )
        if bitmap.get_bit_normalized(i) == 1:
            print( 'we found duplicated the char: {}'.format( ch ) )
            return False
        else:
            bitmap.set_bit( i )


    return True

def ut1( ):
    s = 'abcdef'
    if has_unique_chars( s ):
        print( '"{}", has unique chars'.format( s ) )
    else:
        print( '{}, has duplicated chars'.format( s ) )

def ut2( ):
    s = 'anim@ls from_the-juNgLE'
    if has_unique_chars( s ):
        print( '"{}", has unique chars'.format( s ) )
    else:
        print( '{}, has duplicated chars'.format( s ) )

def ut3():
    size = 5
    idx  = 2    
    b = MyBitmap( size )

    print( '\n begin, current value: {}'.format( b.a ) )
    b.set_bit( idx )
    print( 'get_bit: {}'.format( b.get_bit( idx ) ) )
    print( 'get_bit_normalized: {}'.format( b.get_bit_normalized( idx ) ) )
    print( 'changed value: {}'.format( b.a ) )


    b.unset_bit( idx )
    print( 'get_bit: {}'.format( b.get_bit( idx ) ) )
    print( 'get_bit_normalized: {}'.format( b.get_bit_normalized( idx ) ) )
    print( 'changed value: {}'.format( b.a ) )


# -----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    ut2()
    print( '... end. \n')