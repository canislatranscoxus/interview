'''


links: 

https://en.wikipedia.org/wiki/Counting_sort

'''


def get_key_in_count( value ):
    # This function take as input a value from an array and return the index.
    return value

def counting_sort( input, k  ):
    # input : array or list of positive integers to sort.
    # k     : range of values
    # count : array of k + 1 zeros


    count = [ 0 ] * ( k + 1 )
    output= [ 0 ] * len( input )


    # count number of times a number appears in input array. 
    # The count array  is our histogram now.
    for i in range( 0, len( input) ):
        key = get_key_in_count( input[ i ] )
        count[ key ] = count[ key ] + 1

    print( '\n\n' )
    print( 'input            : {}'.format( input ) )
    print( 'count - histogram: {}'.format( count ) )

    # sumatory
    for i in range( 1, len( count ) ):
        count[ i ] = count[ i ] + count[ i - 1 ]

    print( 'count - summatory: {}'.format( count ) )

    # Fill output array.
    for i in range( len( input ) -1, -1, -1 ):
        
        j = get_key_in_count( input[ i ] )
        count[ j ] = count[ j ] - 1
        output[ count[ j ] ] = input[ i ]


    print( 'output: {}'.format( output ) )
    print( '\n\n' )

    return output



# test 1
input = [ 3, 2, 6, 1, 0 ]
k = max( input )


# test 2
input = [ 3, 2, 6, 2, 1, 2, 3, 0, 2, 10 ]
k = max( input )


output = counting_sort( input, k )