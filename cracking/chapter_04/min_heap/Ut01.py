'''
Unit Test: ut01 - Insert Nodes.

Insert nodes:
    4, 50, 7, 55, 90, 87


the tree most be like this

            4
         /      \
      50         7
     /   \     /   \
   55    90   87    º

insert 2

            4
         /     \
      50        7
     /   \     /   \
   55    90   87    2

after bubble up

            2
         /     \
      50        4
     /   \     /   \
   55    90   87    7
   
'''
import os

from MinHeapBinaryTree  import MinHeapBinaryTree
from Node               import Node

class Ut01:

    dir = '/home/art/Downloads/'
    tree = None

    def test_01(self):
        try:
            a = [4, 50, 7, 55, 90, 87]

            print( 'insert multiple nodes' )
            for i in a:
                n = Node( i )
                self.tree.insert( n )
                print( 'inserting node: {}'.format( i ) )

            g = self.tree.get_graph( )
            file_name = os.path.join( self.dir, 'ut01_g01' )
            self.tree.save_graph( file_name = file_name )

        except Exception as e:
            print( 'test_01(), error: {}'.format( e ) )

    def test_02(self):
        try:
            print( 'Now we insert node 2' )
            n = Node( 2 )
            self.tree.insert( n, sort_bubble_up= True )


            g = self.tree.get_graph( )
            file_name = os.path.join( self.dir, 'ut01_g02' )
            self.tree.save_graph( file_name = file_name )

        except Exception as e:
            print( 'test_02(), error: {}'.format( e ) )

    def __init__(self):
        self.tree = MinHeapBinaryTree()

if __name__ == '__main__':
    t = Ut01()
    t.test_01()
    t.test_02()
    print( '... Unit Test end.' )

