
def update_array( a ):

    num_elements = len( a )
    for i in range( 0, num_elements):
        a[ i ] = a[ i ]  * 10

    print( 'a: {0}'.format( a ) )

# ------------------------------------------------------------------------------------------------
data = [ 1, 2, 3, 4, 5 ]
print( 'original data: {0}'.format( data ) )

update_array( data )
print( 'updated data: {0}'.format( data ) )
