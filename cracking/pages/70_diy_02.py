'''
description:    page 70. Do it your self.

given a small string s, and a big string b,
find all the permutations of s in b.



'''

def is_permutation( s1, s2 ):
    a1 = list(s1)
    a2 = list(s2)

    for ch in a1:
        if ch not in a2:
            return False

        i = a2.index( ch )
        a2.pop( i )

    return True

def find_permutations( s, b ):
    size_s = len( s )
    size_b = len( b )

    for i in range( 0, size_b - size_s + 1 ):
        i_end = i + size_s
        b2          = b[ i  : i_end ]
        if is_permutation( s, b2 ):
            print( '{} : {} , {}'.format( b2, i, i_end ) )
    

if __name__ == '__main__':

    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'
    print( 's: {}'.format( s )  )
    print( 'b: {}'.format( b )  )

    find_permutations( s, b )


