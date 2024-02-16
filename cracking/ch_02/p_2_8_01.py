'''
Question 2.8 Loop Detection

a -> b -> c -> d -> e --+ 
          ^             |
          |             |
          +-------------+

there is a looop from e to c

'''
class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None

class My_list:

    def print_data_list( self, h ):
        n = h
        print( '\n data list:' )
        while n != None:
            print( '{} '.format( n.data), end='' )
            n = n.next
        print( ' *** \n', end='\n' )


    def create_list_from_string( self, a ):
        '''Create a linked list of Node, that has data and next.'''
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



    def has_loop( self, h ):
        d = {}
        n = h
        while n != None:
            if n in d:
                return True
            else:
                d[ n ] = n.data

            n = n.next

        return False


    def find_node( self, h, data ):
        n = h 
        while n != None:
            if n.data == data:
                return n
            
            n = n.next

        return None

    def get_last( self, h ):
        n = h
        while n != None:
            if n.next == None:
                return n
            
            n = n.next



if __name__ == '__main__':

    my_list     = My_list()
    h           = my_list.create_list_from_string( 'abcde' )
    my_list.print_data_list( h )

    c_node      = my_list.find_node( h, 'c' )
    last        = my_list.get_last( h )
    last.next   = c_node
    flag        = my_list.has_loop( h )

    assert flag == True

