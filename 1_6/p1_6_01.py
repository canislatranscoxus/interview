'''
question: 1.6 String Compression

implement a method to perform basic string compression using the counts of repeated character.
For example, the string 

aabcccccaaa would become a2b1c5a3

If the "compressed" string would not become smaller than the original string, 
your method should return the original string.

You can assume the string has only uppercase (A-Z) and lowercase letters (a-z)

'''

def string_compression( s ):
    ch = s[ 0 ]
    a = []
    c = 0
    for i in range( 0, len( s ) ):
        
        if s[ i ] == ch:
            c += 1
        else:
            a.append( ch + str(c) )
            c = 0
            ch = s[ i ]
    
    compressed = ''.join( a )

    if len( compressed ) < len( s ):
        return compressed
    else:
        return s
        

if __name__ == '__main__':
    s = 'aaaaabbbbcccdde'

    compressed = string_compression( s )    

    print( 's: {}'.format( s ) )
    print( 'compressed: {}'.format( compressed ) )
