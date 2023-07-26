
import random

def shell_sort( a ):
    length = len( a )

    gap = length // 2

    while gap > 0:
        for i in range( gap, length ):
            tmp = a[ i ]
            j   = i

            while j >= gap and a[ j - gap ] > tmp :
                a[ j ] = a[ j - gap ]
                j -= gap
                #print( j )

            a[ j ] = tmp
            #print( 'gap: {}, a: {}'.format( gap, a ) )

        gap = gap // 2



data = random.sample( range(0, 100), 10 )

print( '\n\n original data: {}'.format( data ) )
shell_sort( data )
print( 'sorted data: {} \n\n '.format( data ) )
