'''
question 2.5 Sum List

You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are in reverse order, such that the 1's digit is at the head of the list.

write a function that adds the two numbers and return the sum as a linked list.
( You are not allowed to "cheat" and just convert the list to an integer )
example:

  list              Number
-------------    -----------
7 -> 1 -> 6         6 1 7
5 -> 9 -> 2         2 9 5
                 -----------
SUM  =              9 1 2

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
            num = int( ch )
            n   = Node( num )

            if head == None:
                head = n
                last = n
            else:
                last.next = n
                last      = n

        return head


    def add_at_beggining( self, h, n ):
        '''Insert the node n at the beginning of the list. 
        h : head of the list
        n : node        
        '''

        if h == None:
            h = n
        else:
            n.next = h
            h = n
        return h


    def sum_nums( self, carry, x1, x2 ):
        ''' we sum two numbers and a carry. The output is the resulting carry and the digit d.'''
        d = 0
        s = x1 + x2 + carry
        if abs( s ) >= 10:
            carry   = s // 10;
            d       =  s - carry*10
        else:
            carry = 0
            d     = s
        
        return (carry, d)


    def sum_lists( self, h1, h2 ):
        ''' make the sum of list h1 and lst h2, the output is the list result.'''
        result = None
        carry  = 0
        d      = 0
        n1     = h1
        n2     = h2

        # we loop and sum each digit from the lists
        while n1 != None and n2 != None:
            carry, d = self.sum_nums( carry, n1.data, n2.data )
            #print( 'carry: {}, d: {}'.format( carry, d ) )

            n       = Node( d )
            result  = self.add_at_beggining( result, n )       
            n1      = n1.next
            n2      = n2.next

        # check if  one linked list is longer than the other.        
        n = None
        if n1 == None and n2 == None:
            # the two linked list have the same size
            if carry > 0:
                carry, d = self.sum_nums( carry, 0, 0 )
                n = Node( d )
                result = self.add_at_beggining( result, n )
            return result

        elif n1 == None:
            n = n2
        else:
            n = n1

        # we continue summing the rest of the digits of the longer linked list
        d = 0
        while n != None:
            carry, d = self.sum_nums( carry, n.data, 0 )
            node = Node( n.data )
            self.add_at_beggining( result, node )
            n = n.next

        return result


    def _print( self, h ):
        n = h
        print( 'print my list: \n' )
        while n != None:
            print( n.data, end='' )
            n = n.next

        print( ' *** \n', end='\n' )


if __name__ == '__main__':
    my_list = MyList()
    h1 = my_list.create_list_from_string( '716' )
    h2 = my_list.create_list_from_string( '592' )

    my_list._print( h1 )
    my_list._print( h2 )

    result = my_list.sum_lists( h1, h2 )
    my_list._print( result )
