'''
page 94
Chapter 2.

Question 2.1 Write code to remove duplicates from an unsorted linked list.

Follow up.
How would you solve this problem if a temporary buffer is not allowed?

strategy 02:   loop the list once and count freq oc each data.
                loop the list and per each node ask 
                    if data counter > 1 delete node 

time O( n )
Here we are using an extra buffer to store the counters.

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
        #print( 'Linked list \n' )
        while n != None :
            print( ' {}'.format( n.data ), end=' ' )
            n = n.next
        print( '\n ' )

    def get_counters( self ):
        d = dict()
        n = self.head
        while n != None:
            if n.data in d:
                d[ n.data ] = d[ n.data ] + 1
            else:
                d[ n.data ] = 1

            n = n.next
        
        return d


    def delete_node( self, prev, n ):
        if prev == None:
            self.head = self.head.next
        else:
            prev.next = n.next 
        next = n.next

        # delete from memory
        n.next = None
        del n

        n = next


    def remove_dups( self ):
        counters    = self.get_counters()
        n           = self.head
        prev        = None

        while n != None:
            if counters[ n.data ] > 1:
                counters[ n.data ] = counters[ n.data ] -1
                next = n.next
                self.delete_node( prev, n )
                n = next
            else:
                prev = n
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
    my_list._print( )
    my_list.remove_dups()
    
    print( 'Duplicated removed' )
    my_list._print()

    print( '\n ... end.' )