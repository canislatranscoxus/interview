'''
Check permutation: Given two strings, write a method to decide if one is a permutation of the other.

Strategy: use dictionaries, and compare them.

Complexity: O( n )

n + n + n = 3 n ⟹ O(n)

'''

def str_to_dict( s ):
    d = dict()
    for i in s:
        if i in d:
            d[ i ] = d[ i ] + 1
        else:
            d[ i ] = 1

    return d

def are_permutation( s1, s2 ):

    if len( s1 ) != len( s2 ):
        return False

    d1 = str_to_dict( s1 )
    d2 = str_to_dict( s2 )    

    return d1 == d2

def ut1():
    s1 = 'skate board'
    s2 = 'skate park'

    print( 's1: {}'.format( s1 ) )
    print( 's2: {}'.format( s2 ) )

    if are_permutation( s1, s2 ):
        print( 'Yes, they are permutations' )
    else:
        print( 'uuups, they are Not permutations' )


def ut2():
    s1 = 'skate board'
    s2 = 'board skate'

    print( 's1: {}'.format( s1 ) )
    print( 's2: {}'.format( s2 ) )

    if are_permutation( s1, s2 ):
        print( 'Yes, they are permutations' )
    else:
        print( 'uuups, they are Not permutations' )


if __name__ == '__main__':
    print( '\n ... begin \n' )
    ut2()
    print( '\n ... end' )        