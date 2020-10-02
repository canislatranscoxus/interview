'''
Description: write a code that take as input 2 strings that represent
                preorder and inorder of a binary tree. Return as output
                a binary tree.
                See the json.

author: canislatranscoxus
'''

import json
from Binary_tree.BinaryNode import BinaryNode as Node

class Build_tree_01:

    root = None


    def print_tree(self):
        j = {}
        self.add_data_2_json( j, self.root )
        s = json.dumps( j, indent= 4 )
        print( s )

    def add_data_2_json(self, j, n):
        j[ n.data ] = {}
        if   n.left  != None:
            self.add_data_2_json( j[ n.data ], n.left )

        if n.right != None:
            self.add_data_2_json( j[n.data], n.right )





    def __init__( self ):
        print( 'Build_tree_01.__init__()' )

    def run(self, pre_order, in_order):

        preorder = pre_order.split( ',' )
        inorder  = in_order.split( ',' )

        print( 'Build_tree_01.run() ... begin' )

        used_nodes = []
        pre_begin  = 0
        pre_end    = 0
        root       = None
        curr_node  = None

        for in_i in range( 0, len( inorder ) ):
            data = inorder[ in_i ]
            #print( data )

            if data in used_nodes:
                # goto node
                while( curr_node.data != data ):
                    curr_node = curr_node.parent
            else:
                pre_end = preorder.index( data ) + 1

                for i in range( pre_begin, pre_end  ):
                    n = Node( preorder[ i ], parent = curr_node )
                    data2 = n.data
                    used_nodes.append( n.data )
                    if root == None:
                        root      = n
                        curr_node = n
                    elif curr_node.left == None:
                        curr_node.left = n
                        curr_node = curr_node.left
                    else:
                        curr_node.right = n
                        curr_node       = curr_node.right

                pre_begin = pre_end

        self.root = root
        self.print_tree()
        return root



if  __name__ == '__main__':

    preorder = 'F,B,A,D,C,E,G,I,H'
    inorder  = 'A,B,C,D,E,F,G,H,I'

    b = Build_tree_01(  )
    b.run( preorder, inorder )

    print( '... end.' )


