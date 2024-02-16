'''
question 2.2. Return Kth to last.

implement an algorithm to find the kth to last element of a singly linked list.

strategy 1: loop the list and count the number of nodes.
            calculate the position "pos" of the kth node
            loop againg from the list from beginning to pos.

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

    def get_len( self ):
        s = 0
        n = self.head

        while n != None:
            s += 1
            n = n.next
        
        return s


    def get_kth_to_last( self, k ):
        len_list    = self.get_len()
        pos         = len_list - k
        n           = self.head
        next        = self.head

        for i in range( 0, pos ):
            n = next
            next = n.next

        print( 'n.data: {}'.format( n.data ) )
        return n


if __name__ == '__main__':

    a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

    my_list = LinkedList()    
    my_list.add_list_from_array( a )
    
    my_list._print( )
    my_list.get_kth_to_last( k = 3 )
    
    print( '\n ... end.' )