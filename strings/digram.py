# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here

    # strategy
    # find digrams 
    # store the distance between them
    # store the digram with the biggest distance

    max_distance = -1
    digrams = {}

    # we find all the digrams
    # and store the max distances
    for i in range( len(  S )-1  ):
        d = S[ i: i + 2 ]

        if d in digrams:
            # update the position of this new diagram. 
            # This is the furthest distance.
            a = digrams[ d ]
            a[ 1 ] = i

        else:
            # save a new digram, and the position that appear in S.
            a = [ i, 0 ]
            digrams[ d ] = a
        
    # get the Furthest distance
    for k, v in digrams.items():

        if v[1] == 0:
            # this digram is unique. We skip it
            continue

        tmp = v[ 1 ] - v[ 0 ]
        if tmp > max_distance:
            max_distance = tmp

    return max_distance


S = 'aakmaakmakda'
d = solution( S )

print( 'distance: {}'.format( d )  )