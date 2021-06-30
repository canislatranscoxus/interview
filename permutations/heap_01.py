'''
description: this is the Heap's algorithm that print all the permutations with
                no duplicated and is recursive.

links:
https://en.wikipedia.org/wiki/Heap%27s_algorithm
'''


def _print( objs ):
    for i in objs:
        print( i, end=' ' )
    print( ' ' )

def swap( objs, idx1, idx2 ):
    objs[ idx1 ],  objs[ idx2 ] = objs[ idx2 ],  objs[ idx1 ]


def generate(k, a):
    if k == 1 :
        _print( a )
    else:
        # Generate permutations with kth unaltered
        # Initially k == len( a )
        #generate(k - 1, a)

        # Generate permutations for kth swapped with each k-1 initial
        for i in range( 0, k ):
            generate( k - 1, a )
            # Swap choice dependent on parity of k (even or odd)
            if k % 2 == 0 :
                swap( a, i, k-1 ) # zero-indexed, the kth is at k-1
            else:
                swap( a, 0, k-1 )

            #_print( a )        
            

        
    


    

def ut_01():
    objs = [ 'apple', 'banana', 'orange' ]
    #objs = [ 'apple', 'banana', 'orange', 'lemon', 'mango' ]
    generate( len(objs),  objs )

def ut_02():
    s = 'abcd'
    a = [ i for i in s ]
    generate( len(a), a )

def ut_03():
    objs = [ 'apple', 'banana', 'orange', 'lemon', 'mango' ]
    _print( objs )
    swap( objs, 0, 3 )
    _print( objs )

if __name__ == '__main__':
    print( '\n heap algorithm, begin. \n\n' )
    ut_01()
    print( '\n heap algorithm, end. \n\n' )
