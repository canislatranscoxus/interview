"""
Write a function that returns the elements on odd positions (0 based) in a list
"""
def solution(input):
    #code goes here

    output = []

    for i in range(1, len(input), 2 ):
        output.append( input[ i ]  )

    return output

# --------------------------------------

input  = [ 0, 10, 20, 30, 40, 50, 70, 80, 90, 100 ]
output = solution( input )
print( 'input  list: {}'.format( input ) )
print( 'output list: {}'.format( output) )


assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]