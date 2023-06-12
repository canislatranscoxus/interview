'''
Binary Heaps ( Min Max Heap Trees )
Page: 103.

Here we implement a Binary Heap - Min Heap Tree.
with its 2 functions:

* Insert() and
* get_min_value()

We create a class to handle all that. And also,
we generate a Visual graph in pdf, svg, png, ...

'''

from .Node import Node

class MinHeapBinaryTree:

    # first highest leaf
    fh_leaf       = None
    fh_leaf_level = 0

    def insert( self, n ):
        try:
            if root == None:
                root = n
                return
            
            p = self.find_free_slot( n )

            # add node
            if p.left == None:
                p.left   = n
                n.parent = p
            else:
                p.right  = n
                n.parent = p.right

            self.bubble_up( n )

        except Exception as e:
            print( 'MinHeapBinaryTree.insert(), error: '.format( e ) )
            
    def extract_min_value( self ):
        pass

    def find_free_slot( self, n, level ):
        # this method finds the node that has 1 or 2 free slots.
        # it means, the node that can be parent of a node.
         
        try:
            if n == None:
                return None
            
            elif n.left != None and n.right == None:
                # parent of 1
                return n
            
            elif self.is_leaf( n ):
                if self.fh_leaf == None or level < self.fh_leaf_level:
                    self.fh_leaf       = n
                    self.fh_leaf_level = level
                
                #return None

            elif n.left != None and n.right != None:
                # has 2 child
                l = self.find_free_slot( n.left , level + 1 )
                r = self.find_free_slot( n.right, level + 1 )
                
                if l != None:
                    return l
                elif r != None:
                    return r
                
            return self.fh_leaf

        except Exception as e:
            print( 'MinHeapBinaryTree.find_free_slot(), error: '.format( e ) )


    def bubble_up( self, n ):
        try:
            if n.parent == None:
                print( 'bubble up end' )
                return
            
            if n.value < n.parent.value:
                self.swap( n.parent, n )
            
            self.bubble_up( n )

        except Exception as e:
            print( 'MinHeapBinaryTree.bubble_up(), error: '.format( e ) )


    def bubble_down( self, n ):
        try:
            if n == None or self.is_leaf( n ):
                return
            

            #todo: fix this
            '''
            if n.left != None and n.left.value < n.value:
                self.swap( n, n.left ) 

            if n.right != None and n.left.value < n.value:
                self.swap( n, n.right )
            '''

        except Exception as e:
            print( 'MinHeapBinaryTree.bubble_down(), error: '.format( e ) )


    def swap( self, parent, child ):
        try:
            _left  = parent.left
            _right = parent.right
            parent.left  = child.left
            parent.right = child.right
            child.left  = _left 
            child.right = _right

            child.parent = parent.parent
            parent.parent = child
        except Exception as e:
            print( 'MinHeapBinaryTree.swap(), error: '.format( e ) )


    def is_leaf( self, n ):
        if n != None and n.left == None and n.right == None:
            return True
        
        return False
    
    # Visual Graph with graphviz

    def get_graph( self ):
        pass

    def add_node_2_graph( self, g, n ):
        pass

    def add_edge_2_graph( self ):
        pass

    def save_graph( self, file_name, format = 'pdf' ):
        pass