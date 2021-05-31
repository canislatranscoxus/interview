""" From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and 
smallest values in the array. If there are multiple copies of the 
smallest value, ignore just one copy, and likewise for the largest 
value. Use int division to produce the final average. You may assume 
that the array is length 3 or more.
"""

def solution(input):

    input.sort()
    input.pop()
    input.pop(0)
    s = sum( input )
    n = len( input )
    output = s // n

    return output 

assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3


def solution2(input):
    s = 0
    mini = input[ 0 ]
    maxi = input[ 0 ]
    for i in input:
        s = s + i
        # find minimum
        if i < mini:
            mini = i

        # find maximum
        if i > maxi:
                maxi = i

    # remove minimum adn max
    s = s - mini - maxi

    # do average
    n = len( input ) -2
    output = s // n

    return output 

assert solution2([1, 2, 3, 4, 100]) == 3
assert solution2([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution2([-10, -4, -2, -4, -2, 0]) == -3

