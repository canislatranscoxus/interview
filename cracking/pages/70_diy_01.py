'''
description:    page 70. Do it your self.

given a small string s, and a big string b,
find all the permutations of s in b.



'''

def sort_str( s ):
    # sort a string
    a = sorted( s )
    z = ''.join( a )
    return z


def is_permutation(s2, b2):
    # check if b2 is permutation of s2
    # s2 = sorted    string
    # b3 = unordered string
    sorted_b2   = sort_str( b2 )
    if s2 == sorted_b2:
        return True
    else:
        return False


def find_permutations( s, b ):
    s2      = sort_str( s )
    size_s  = len( s )
    size_b  = len( b )

    for i in range( 0, size_b - size_s + 1 ):
        i_end   = i + size_s
        b2      = b[ i  : i_end ]
        if is_permutation( s2, b2 ):
            print( '{} : {} , {}'.format( b2, i, i_end ) )
    

if __name__ == '__main__':

    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'
    print( 's: {}'.format( s )  )
    print( 'b: {}'.format( b )  )

    find_permutations( s, b )


