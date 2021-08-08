'''
Find the positive integers from 0 to 100 for


Equation E1

  3      3       3       3
 a  +   b   =   c   +   d

where:
   a <> b

My reasoning is, 

calculate all the (a3 + b3) from 0 to N,
and store  in cache,
next loop the cache and print all the pairs  

'''

def powers_1_to_n( n, p ):
    # this function loop from 1 to n, and create a dictionary of powers
    # and its pair of powers.
    # 
    # n       = is the maximum limit number
    # p       = is the exponent for the power function
    # powers  = a dictionary that store key values.
    #             key is a number from 1 to n.
    #             value the power of number.                    

    powers = dict()
    for i in range( 1, n + 1 ):
        powers[ i ] = pow( i, p )
    return powers


# a3 + b3
def get_sum_pow( powers ):
    sum_pow = dict()
    for a in range( 1, n ):
        for b in range( a + 1, n + 1):
            s    = powers[ a ] + powers[ b ]
            pair = ( a, b )

            if s in sum_pow:
                sum_pow[ s ].add( pair )
            else:
                pairs = set()
                pairs.add( pair )
                sum_pow[ s ] = pairs

    return sum_pow


def find_abcd( n ):
    p       = 3
    powers  = powers_1_to_n( n, p )
    sum_pow = get_sum_pow( powers )

    for s, pairs in sum_pow.items():
        if len( pairs ) > 1:
            print( 'a^3 + b^3 = {:>15,} --- {}'.format( s, pairs ) )

if __name__ == '__main__':

    n = 1000
    print( '\n\n ...begin.' )
    print( 'Given equation \n\n a^3 + b^3 = c^3 + d^3    \n\n find a, b, c, b.' )

    find_abcd( n )
    print( '\n\n ...end' )

    