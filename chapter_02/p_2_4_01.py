'''
question 2.4. Partition.

Write code to partition a linked list around a value x, such that all nodes less than x
come before all nodes greater than or equal to x.

( IMPORTANT: the partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.

The additional spacing in the example below indicates the partition. 
Yes, the output below is one of many valid outputs! )

example:

input   : 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1  [ partition = 5 ]
output  : 3 -> 1 -> 2           ->            10 -> 5 -> 5 -> 8  

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


    def remove_node( self, prev, n ):
        # remove node from list. But do not delete from memory
        if prev == None:
            self.head = n.next
        else:
            prev.next = n.next
        
        n.next = None


    def insert_node( self, first, n ):
        if first == None:
            first = n
        else:
            n.next = first
            first = n
        
        return first


    def concat_lists( self, h1, h2 ):
        n = h1

        while n.next != None:
            n = n.next

        n.next = h2

    def get_partition_list( self, partition_data ):
        left  = None
        right = None

        prev  = None
        n     = self.head


        while n != None:
            next = n.next
            self.remove_node( prev, n )

            if n.data < partition_data:
              left  = self.insert_node( left, n )
            else:
              right = self.insert_node( right, n )

            n = next

        self.concat_lists( left, right )
        self.head = left








if __name__ == '__main__':

    a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    #a = [ 1   ]

    my_list = LinkedList()    
    my_list.add_list_from_array( a )

    print( '\n original list' )     
    my_list._print( )

    my_list.get_partition_list( 5 )
    print( '\n partitioned list' )     
    my_list._print( )
    print( '\n ... end.' )