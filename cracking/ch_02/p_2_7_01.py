'''
Question 2.7 Intersection



'''




class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None

class RNode:
    ref  = None
    next = None
    
    def __init__(self, ref ):
        self.ref = ref
        self.next = None    
    

class My_list:


    def print_data_list( self, h ):
        n = h
        print( '\n data list:' )
        while n != None:
            print( '{} '.format( n.data), end='' )
            n = n.next
        print( ' *** \n', end='\n' )


    def print_ref_list( self, h ):
        n = h
        while n != None:
            print( '{} '.format( n.ref.data ), end='' )
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

    def find_node( self, h, data ):
        n = h 
        while n != None:
            if n.data == data:
                return n
            
            n = n.next

        return None


    def create_rlist( self, head_data_nodes, str_ref_nodes ):
        '''Create a linked list of Referenced Nodes.'''
        head = None
        last = None

        for ch in str_ref_nodes:
            ref = self.find_node( head_data_nodes, ch )
            n = RNode( ref )
            if head == None:
                head = n
                last = n
            else:
                last.next = n
                last      = n

        return head

    def get_ref_nodes( self, h ):
        '''Get a dictionary with all the referenced nodes in the linked list'''

        d = {}
        n = h
        while n != None:
            if n.ref not in d:
                d[ n.ref ] = n.ref
            
            n = n.next
        
        return d


    def add_to_rlist( self, h, data_node):
        n       = RNode( data_node )
        if h == None:
            h = n
        else:
            n.next = h
            h = n
        
        return h

    def get_intersection( self, h1, h2 ):
        inter = None
        d1 = self.get_ref_nodes( h1 )
        d2 = self.get_ref_nodes( h2 )

        for ref1 in d1.keys():
            if ref1 in d2:
                n = d1[ ref1 ]
                inter = self.add_to_rlist( inter, n )

        return inter


if __name__ == '__main__':

    my_list = My_list()
    data_nodes = my_list.create_list_from_string( 'abcdefghi' )

    my_list.print_data_list( data_nodes )

    h1 = my_list.create_rlist( data_nodes, 'abdegh' )
    h2 = my_list.create_rlist( data_nodes, 'bcefhi' )

    print( 'ref list h1 ' )
    my_list.print_ref_list( h1 )

    print( 'ref list h2 ' )
    my_list.print_ref_list( h2 )

    inter = my_list.get_intersection( h1, h2 )

    print( 'list with interseting nodes' )
    my_list.print_ref_list( inter )