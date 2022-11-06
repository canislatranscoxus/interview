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

strategy: use just one array. The original array.

Complexity: O( n )

n = parameter size
n + n + n = 3n ==> O(n)

'''

class URL_converter:

    separator       = '%20'
    separator_size  = 3


    def copy_sep( self, a, i_start ):
        for i in range( self.separator_size ):
            a[ i_start + i ] = self.separator[ i ]

    def move_to_right( self, a, m, i_start, i_end ):
        for i in range( i_end, i_start -1, -1 ):
            a[ i + m ] = a[ i ] 

    def move_to_left( self, a, m, i_start, i_end ):
        for i in range( i_start, i_end ):
            a[ i ] = a[ i + m ] 


    def insert_separator( self, a, i_start, idx_last ):
        # count num of spaces
        num_spaces = 0
        for i in range( i_start, idx_last ):
            if a[ i ] != ' ':
                break
            
            num_spaces += 1

        if num_spaces == self.separator_size:
            self.copy_sep( a, i_start )    
        if num_spaces < self.separator_size:
            m = self.separator_size - num_spaces
            self.move_to_right( a, m, i_start + 1, idx_last )
            self.copy_sep( a, i_start )    
            idx_last += m 
        else:
            # num_spaces > self.separator_size:
            m = num_spaces - self.separator_size
            self.copy_sep( a, i_start )    
            self.move_to_left( a, m, i_start + m - 1, idx_last )
            idx_last -= m 

        return idx_last



    def urlify( self, s, text_size ):

        a = list( s )
        idx_last = text_size - 1
        i = 0 
        while i < idx_last:
            ch = a[ i ]
            if ch == ' ':
                idx_last = self.insert_separator( a, i, idx_last )
            
            i = i + 1

        result = a[ : idx_last ]
        return result



    def __init__( self ):
        self.separator = '%20'
        self.separator_size = 3



def ut1():
    #s = 'Mr John Smith        '
    #size = 13

    s = '  Mr   John   Smith        '
    size = 19

    a = list( s )

    url_converter = URL_converter()

    a2 = url_converter.urlify( s, size )
    print( 'my string: "{}"'.format( a ) )
    print( 'my url   : "{}"'.format( a2 ) )

if __name__ == '__main__':
    print( '\n... begin.' )    
    ut1()
    print( '\n... end.' )    



