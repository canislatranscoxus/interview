'''
Question 2.6 Palindrome

Implement a function to check if a linked list is a palindrome.

Strategy 2. Do not use array or other data structure

O( n + n * n/2  ) --> O( n + n^2 ) --> O( n ^ 2 )
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


    def get_size( self, h ):
        s = 0
        n = h
        while n != None:
            s += 1
            n = n.next
        return s

    def get_data( self, h, pos ):
        i = 0
        n = h
        for i in range( 0, pos ):
            n = n.next

        if n == None:
            return None
        else:
            return n.data



    def is_palindrome( self, h ):
        size = self.get_size( h )
        for i in range( 0, size // 2 ):
            d1 = self.get_data( h, i ) 
            d2 = self.get_data( h, size - i - 1 ) 
            if d1 != d2:
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