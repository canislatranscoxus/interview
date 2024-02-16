'''
Check permutation: Given two strings, write a method to decide if one is a permutation of the other.

Strategy: use lists, sort them and compare them.

Complexity: O( n )

n + nlog( n ) + n + nlog( n ) + n = 3n + 3 nlog( n ) ⟹ O( n log n )

'''



def are_permutation( s1, s2 ):

    if len( s1 ) != len( s2 ):
        return False

    a1 = list( s1 )
    a2 = list( s2 )
    a1.sort()
    a2.sort()
    return a1 == a2

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
    ut1()
    print( '\n ... end' )        