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

    def _print( self, n=None ):

        if n == None:
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

    def append( self, last, n ):
        if last == None:
            last = n
        else:
            last.next = n
        
        return n

    def concat_lists( self, h1, h2 ):
        n = h1

        while n.next != None:
            n = n.next

        n.next = h2

    def get_partition_list( self, partition_data ):
        left  = None
        right = None
        right_last = None

        prev  = None
        n     = self.head


        while n != None:
            next = n.next
            self.remove_node( prev, n )

            if   n.data <  partition_data:
              left  = self.insert_node( left, n )

            elif n.data == partition_data:
              right = self.insert_node( right, n )
              if right_last == None:
                  right_last = right 
            else:
                right_last = self.append( right_last, n )
                if right == None:
                    right = n

            n = next

        print( 'left' )
        self._print( left )

        print( 'right' )
        self._print( right )

        self.concat_lists( left, right )
        self.head = left








if __name__ == '__main__':

    a = [ 9, 6, 5, 2, 3, 10, 8, 5, 6, 7, 4 ]
    #a = [ 1   ]

    partition_data = 5

    my_list = LinkedList()    
    my_list.add_list_from_array( a )

    print( '\n original list' )     
    my_list._print( )

    my_list.get_partition_list( partition_data )
    print( '\n partitioned list' )     
    my_list._print( )
    print( '\n ... end.' )