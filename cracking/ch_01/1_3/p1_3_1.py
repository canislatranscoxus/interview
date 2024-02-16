'''
Interview Question

1.3 URLify: 

Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the
"true" length of the string. ( Note: if implementing in java, please use a character array so
that you can perform this operation in place ).

EXAMPLE: 
Input : "Mr John Smith        ", 13
Output: "Mr%20John%20Smith"

strategy: use list and a new string

Complexity: O( n )

n = parameter size
n + n + n = 3n ==> O(n)

'''

def urlify( s, size ):

    s = s[ : size - 1 ]
    a = s.split( )
    s = '%20'.join( a )
    return s

def ut1():
    #s = 'Mr John Smith        '
    #size = 13

    s = '  Mr   John   Smith        '
    size = 19
    s2 = urlify( s, size )
    print( 'my string: "{}"'.format( s) )
    print( 'my url   : "{}"'.format( s2 ) )

if __name__ == '__main__':
    print( '\n... begin.' )    
    ut1()
    print( '\n... end.' )    



