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

import graphviz



from Node import Node

class MinHeapBinaryTree:
    LEFT_CHILD    = 0
    RIGHT_CHILD   = 1
    last_node_id  = -1
    root          = None

    # first highest leaf
    fh_leaf       = None
    fh_leaf_level = 0



    graph         = None

    def insert( self, n, sort_bubble_up = True ):
        try:
            self.last_node_id = self.last_node_id + 1
            n.id              = self.last_node_id

            if self.root == None:
                self.root         = n
                return

            self.fh_leaf = None
            p = self.find_free_slot( self.root, level= 0 )
            if p == None:
                p = self.fh_leaf
            
            # add node
            if p.left == None:
                p.left   = n
                n.parent = p
            else:
                p.right  = n
                n.parent = p

            if sort_bubble_up:
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

                return None

            elif n.left != None and n.right != None:
                # has 2 child
                l = self.find_free_slot( n.left , level + 1 )
                r = self.find_free_slot( n.right, level + 1 )
                
                if l != None:
                    return l
                elif r != None:
                    return r
                
            return None

        except Exception as e:
            print( 'MinHeapBinaryTree.find_free_slot(), error: '.format( e ) )


    def bubble_up( self, n ):
        try:
            if n.parent == None:
                self.root = n
                print( 'bubble up end' )
                return
            
            if n.value < n.parent.value:
                self.swap( n.parent, n )
                self.bubble_up( n )

        except Exception as e:
            print( 'MinHeapBinaryTree.bubble_up(), error: '.format( e ) )


    def get_smallest_child( self, n ):
        
        if n == None or (n.left == None or n.right == None):
            return None
        
        if (n.left != None and n.right == None) or \
            n.left <= n.right:
            return self.LEFT_CHILD
        else:
            return self.RIGHT_CHILD 
        
    def bubble_down( self, n ):
        try:
            if n == None or self.is_leaf( n ):
                return
            
            youngest = self.get_smallest_child( n )

            if youngest == self.LEFT_CHILD:
                self.swap( n, n.left  )
            else:
                self.swap( n, n.right )

        except Exception as e:
            print( 'MinHeapBinaryTree.bubble_down(), error: '.format( e ) )


    def swap( self, parent, child ):
        try:
            _left  = parent.left
            _right = parent.right
            _parent= parent.parent

            parent.left  = child.left
            parent.right = child.right

            if _left == child:
                child.left  = parent
                child.right = _right
            else:
                child.right = parent
                child.left  = _left


            parent.parent = child

            child.parent = _parent
            if _parent.left == parent:
                _parent.left = child
            else:
                _parent.right = child

        except Exception as e:
            print( 'MinHeapBinaryTree.swap(), error: '.format( e ) )


    def is_leaf( self, n ):
        if n != None and n.left == None and n.right == None:
            return True
        
        return False


    #┌────────────────────────────────────────────────────────────────────────┐
    #│                   Visual Graph with graphviz                           │
    #└────────────────────────────────────────────────────────────────────────┘

    def get_graph( self, comment = 'Min Heap Binary Tree', format= 'pdf' ):
        try:
            self.graph = graphviz.Digraph(comment= comment, format = format )

            # Graph Orientation:
            #   LR = horizontal
            #   TB = vertical

            #self.graph.attr('graph', rankdir='TB')
            self.graph.attr( rankdir='TB' )

            self.add_node_2_graph( self.graph, self.root )
            self.add_edge_2_graph( self.graph, self.root )
            return self.graph
        
        except Exception as e:
            print( 'get_graph(), error: {}'.format( e ) )

    def add_node_2_graph( self, g, n ):
        try:
            if n == None:
                return None
            
            g.node( str( n.id ), str( n.value ) )

            self.add_node_2_graph( g, n.left  )
            self.add_node_2_graph( g, n.right )
            
        except Exception as e:
            print( 'add_node_2_graph(), error: {}'.format( e ) )


    def add_edge_2_graph( self, g, n ):
        try:
            if n == None:
                return
            
            if n.left != None:
                #g.edge( str( n.id ), str( n.left.id ), constraint = 'false' )
                g.edge(str(n.id), str(n.left.id) )
                self.add_edge_2_graph( g, n.left )

            if n.right != None:
                #g.edge( str( n.id ), str( n.right.id ), constraint = 'false' )
                g.edge(str(n.id), str(n.right.id) )
                self.add_edge_2_graph( g, n.right )

            
        except Exception as e:
            print( 'add_edge_2_graph(), error: {}'.format( e ) )


    def save_graph( self, file_name, format = 'pdf' ):
        try:
            if self.graph == None:
                self.get_graph()

            self.graph.render( file_name, view = True, format = format )

        except Exception as e:
            print( 'save_graph(), error: {}'.format( e ) )
