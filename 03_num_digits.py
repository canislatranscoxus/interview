"""
Write a function that takes a number and returns a list of its digits
"""
def solution(input):

    output = []

    while input >= 10:
        r = input % 10
        input = input // 10
        output.insert(0, r)
    
    output.insert( 0, input )

    return output

assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]


def solution2(input):

    a = str( input).replace( '-', '' ).replace( '.', '' )
    output = []

    for i in a:
        n = int( i )
        output.append( n )

    return output

assert solution2(123) == [1,2,3]
assert solution2(400) == [4,0,0]

