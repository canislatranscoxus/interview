'''
Question 2.6 Palindrome

Implement a function to check if a linked list is a palindrome.

Strategy 1. Convert to array and check string palindrome.
'''

class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None


class MyList:

    def create_list_from_string( self, a ):
        head = None
        last = None

        for ch in a:
            n   = Node( ch )

            if head == None:
                head = n
                last = n
            else:
                last.next = n
                last      = n

        return head

    def is_palindrome( self, h ):
        a = []
        n = h
        while n != None:
            a.append( n.data )
            n = n.next

        size = len( a )
        for i in range( 0, size ):
            if a[ i ] != a[ size - i - 1]:
                return False

        return True


if __name__ == '__main__':
    my_list = MyList()

    #s = 'asdf*fdsa' # Palindrome
    s = 'abcy)cba' # Not palindrome

    print( '\n s: {} \n'.format( s ) )
    h = my_list.create_list_from_string( s )
    flag = my_list.is_palindrome( h )

    assert flag == False