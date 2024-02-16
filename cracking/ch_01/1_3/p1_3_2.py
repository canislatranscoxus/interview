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

strategy: use array and a new string

Complexity: O( n )

n = parameter size
n + n + n = 3n ==> O(n)

'''

def urlify( s, size ):

    s = s[ : size - 1 ]
    print( 'trimmed string: {}'.format( s ) )    
    a = []
    word = ''
    # extract words
    for ch in s:
        if ch == ' ':
            if word != '':
                a.append( word )
                word = ''
        else:
            word = word + ch
    if word != '':
        a.append( word )
    s2 = '%20'.join( a )
    return s2

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



