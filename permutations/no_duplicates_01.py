'''
Description: this script print all the permutations with NO duplicates.
                For example: when runners in a race, you can no arrive first and third place.

    here we handle the permutations like a secuence of numbers. We want to print from 
    smaller to bigger. Each number can represent a runner, and each permutation has a 
    relationship with a number in the secuence.

    0 1 2 3
    0 1 3 2
    0 2 1 3
    0 2 3 1
    0 3 1 2
    0 3 2 1

    1 0 2 3
    1 0 3 2
    1 2 0 3
    1 2 3 0
    1 3 0 2
    1 3 2 0

    3 0 1 2
    3 0 2 1
    3 1 0 3
    3 1 3 0
    3 2 0 1
    3 2 1 0



'''

def _print( objs ):
    for i in objs:
        print( i, end=' ' )
    print( ' ' )

def swift_last_2( objs ):
    tmp = objs[ -1 ]
    objs[ -1 ] = objs[ -2 ] 
    objs[ -2 ] = tmp

def change_in_col( objs, col ):
    col_changed = False
    size = len( objs )

    while col >=0 and col_changed == False :

        # get the last part of the array 
        a = objs[ col + 1:  ]

        # sort the las part of the array
        a.sort()
        for i in range( size -1, col, -1 ):
            del objs[ i ]
        objs.extend( a ) 

        #find the next element we need in col
        for i in range( col + 1, size ):
            if objs[ i ] > objs[ col ]:
                tmp         = objs[ col ]
                objs[ col ] = objs[ i ]
                objs[ i   ] = tmp 
                col_changed = True
                break

        col = col - 1
    return col_changed


def permutation( objs  ):
    objs.sort()
    size = len( objs )
    col  = size - 3
    if size <= 1:
        _print( objs )
        return
    
    col_changed = True
    while col_changed == True:
    
        _print( objs )
        swift_last_2( objs )
        _print( objs )
        col_changed = change_in_col( objs, col )    
        


def str_permutation( my_string ):
    a = []
    for i in my_string:
        a.append( i )
    permutation( a )


def ut_01():
    objs = [ 'apple', 'banana', 'orange', 'lemon', 'mango' ]
    permutation( objs )

def ut_02():
    s = 'abcd'
    str_permutation( s )
    
def ut_03():
    objs = [ 0, 1, 2, 3, 4, 5 ]
    permutation( objs )


if __name__ == '__main__':
    print( '\n begin ... \n\n' )
    ut_03()
    print( '\n\n ...end \n' )
