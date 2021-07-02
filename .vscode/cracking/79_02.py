'''
description: functions that check if two numbers passed as strings are equal.
             , one string represents a binary number 
             and the other represent an hexadecimal
'''

def convert_str_to_decimal( s, base ):
    #
    
    if base == 16:
        s = s.upper()
        a = list( s.strip() )
        s = ','.join( a )
        for i in range( ord( 'A' ), ord( 'F' ) + 1 ):
            s = s.replace( chr(i), str( i- ord('A')+10 ) )
        a = s.split( ',' )
    else:
        a = list( s.strip() )
        

    size = len( a )
    e = 0
    n = 0
    for i in range( size -1, -1, -1 ):
        e = size -1 -i
        x = int( a[ i ] )
        n = n + x * pow( base, e )

    return n


def _equal( bin, hex ):
    n1 = convert_str_to_decimal( bin, 2 )
    n2 = convert_str_to_decimal( hex, 16 )
    
    print( 'bin to decimal: {:,} ; hex to decimal: {:,}'.format( n1, n2) )
    
    return n1 == n2

if __name__ == '__main__':
    # decimal 2587
    bin = '101000011011'
    hex = 'A1B'
    comparison = _equal( bin, hex )
    print( '\n\n is {} == {} ? {} \n\n'.format( bin, hex, comparison ) )
    