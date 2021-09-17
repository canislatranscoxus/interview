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
    # this function loop from 1 to n, and create a dictionary of sum of powers
    # and its pair of powers.
    # 
    # n       = is the maximum limit number
    # p       = is the exponent for the power function
    # i, j    = are indexes used to loop from 1 to n.  
    # sum_pow =   i^p + j^p
    # powers  = a dictionary that store key values.
    #             key is a sum_pow
    #             value a set of pairs                    

    powers = dict()
    for i in range( 1, n ):
        for j in range( i + 1, n + 1):
            sum_pow  = pow( i, p ) + pow( j, p)
            pair        = ( i, j )

            if sum_pow in powers:
                powers[ sum_pow ].add( pair )
            else:
                pairs = set()
                pairs.add( pair )
                powers[ sum_pow ] = pairs

    return powers

def find_abcd( n ):
    p      = 3
    powers = powers_1_to_n( n, p )
    for sum_pow, pairs in powers.items():
        if len( pairs ) > 1:
            print( 'a^3 + b^3 = {:>15,} --- {}'.format( sum_pow, pairs ) )

if __name__ == '__main__':

    n = 1000
    print( '\n\n ...begin.' )
    print( 'Given equation \n\n a^3 + b^3 = c^3 + d^3    \n\n find a, b, c, b.' )

    find_abcd( n )
    print( '\n\n ...end' )

    