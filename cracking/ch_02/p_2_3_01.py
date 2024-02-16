'''
question 2.3. Delete middle node.

implement an algorithm to delete a node in the middle (ie any node but
the first and the last node , not necesary the exact middle) of a singly 
linked list, given only access to that node.

Example
input:  a b c d e f
output: a b   d e f

strategy 1: .

'''
import math

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

    def del_node( self, prev, n ):

        if prev == None:
            self.head = n.next
        else:
            prev.next = n.next

        n.next = None
        del n


    def delete_middle_node( self ):
        len_list    = self.get_len()

        if len_list == 1:
            print( 'the linked list has just 1 node. We do not delete it.' )
            return

        m           = math.ceil( len_list / 2 )
        prev        = None
        n           = None
        next        = self.head

        for i in range( 0, m ):
            prev = n
            n = next
            next = n.next

        print( 'deleting... {}'.format( n.data ) )
        self.del_node( prev, n )




if __name__ == '__main__':

    #a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    a = [ 1   ]

    my_list = LinkedList()    
    my_list.add_list_from_array( a )

    print( '\n original list' )     
    my_list._print( )

    my_list.delete_middle_node()
    print( '\n middle node deleted' )     
    my_list._print( )
    print( '\n ... end.' )