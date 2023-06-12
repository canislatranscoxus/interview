'''
find the longest sequence of ceros in a binary
'''

def find_max_sequence( s ):
    max_start = None
    max_size  = 0

    current_size = 0
    is_cero = False

    for i in range( 0, len( s )  ):
        if s[i] == '0':
            current_size = current_size + 1
        else:
            if max_size == None or current_size > max_size:
                max_size = current_size
                max_start = i 
                current_size = 0

    print( 'max_size: {}'.format( max_size ) )
    print( 'max_start: {}'.format( max_start ) )

    sequence = '0' * max_size
    return sequence



s = '1010100011100000011111110000'        
seq =  find_max_sequence( s )
print( 'seq: {}'.format( seq ) )