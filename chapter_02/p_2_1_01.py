'''
page 94
Chapter 2.

Question 2.1 Write code to remove duplicates from an unsorted linked list.

Follow up.
How would you solve this problem if a temporary buffer is not allowed?

startegy:   for each node, delete nodes == data from the sublist 
            starting with the next node.

time O( n ^2 )

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
        print( 'Linked list \n' )
        while n != None :
            print( n.data )
            n = n.next

    def del_node( self, head, start, data ):
        prev = head
        n = start
        while n != None:
            if n.data == data:
                prev.next = n.next

                # delete node from memory
                n.next = None
                del n

                n = prev.next
            else:
                prev    = n
                n       = n.next


    def remove_dups( self ):
        n    = self.head
        prev = None

        if self.head == None:
            return None

        while n != None:
            #print( 'deleting ... {}'.format( n.data ) )
            self.del_node( n, n.next, n.data )
            n = n.next


    def add_list_from_array( self, a ):
        for i in a:
            n = Node( i )

            if self.head == None:
                self.head = n
                self.last = n
            else:
                self.last.next = n
                self.last      = n



if __name__ == '__main__':

    a = [ 1, 2, 7, 3, 4, 1, 3, 7, 5, 6, 3, 8 ]
    my_list = LinkedList()    
    my_list.add_list_from_array( a )
    
    print( 'original' )
    my_list._print()
    my_list.remove_dups()
    
    print( 'Duplicated removed' )
    my_list._print()

    print( '\n ... end.' )