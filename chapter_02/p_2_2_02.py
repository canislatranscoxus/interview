'''
question 2.2. Return Kth to last.

implement an algorithm to find the kth to last element of a singly linked list.

strategy 2: recursive

O( n ) where n is the length of the linked list


'''

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None
    last = None

    def _print( self ):
        n = self.head
        while n != None :
            print( ' {}'.format( n.data ), end=' ' )
            n = n.next
        print( '\n ' )

    def add_list_from_array( self, a ):
        for i in a:
            n = Node( i )

            if self.head == None:
                self.head = n
                self.last = n
            else:
                self.last.next = n
                self.last      = n


    def is_k_node(self, n , k ):

        if n == None or k < 0:
            return False

        if k == 0 and n.next == None:
            return True
        elif self.is_k_node( n.next, k - 1 ):
            return True
        else:
            return False
            


    def get_kth_to_last( self, k ):
        n           = self.head

        while n != None:
            if self.is_k_node( n, k ):
                break

            n = n.next
            

        print( 'n.data: {}'.format( n.data ) )
        return n


if __name__ == '__main__':

    a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    #a = [ 1, 2, 3, 4, 5 ]

    my_list = LinkedList()    
    my_list.add_list_from_array( a )
    
    my_list._print( )
    my_list.get_kth_to_last( k = 3 )
    
    print( '\n ... end.' )