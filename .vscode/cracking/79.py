'''
description: functions that check if two numbers passed as strings are equal.
             , one string represents a binary number 
             and the other represent an hexadecimal
'''



def _equal( bin, hex ):
    n1 = int( bin, 2 )
    n2 = int( hex, 16 )
    
    print( 'bin to decimal: {:,} ; hex to decimal: {:,}'.format( n1, n2) )
    
    return n1 == n2

if __name__ == '__main__':
    bin = '101000011011'
    hex = 'A1B'
    comparison = _equal( bin, hex )
    print( '\n\n is {} == {} ? {} \n\n'.format( bin, hex, comparison ) )
    