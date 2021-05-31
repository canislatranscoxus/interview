"""
Write a function that returns the cumulative sum of elements in a list
"""
def solution(input):

    s = 0
    output = []

    for i in input:
        s = s + i
        output.append( s )

    return output

assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]
