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

class Ut02:
    dir = '/home/art/Downloads/'
    tree = None

    def test_01( self  ):
        try:
            print( 'insert multiple nodes' )
            a = [13, 69, 74, 88, 99, 32, 23]

            for i in a:
                n = Node( i )
                self.tree.insert( n )
                print( 'inserting node: {}'.format( i ) )

            g = self.tree.get_graph( )
            file_name = os.path.join( self.dir, 'ut02_g01' )
            self.tree.save_graph( file_name = file_name )

        except Exception as e:
            print( 'test_01(), error: {}'.format( e ) )


    def test_02( self ):
        try:
            print( 'Now we insert node 96' )
            n = Node( 96 )
            self.tree.insert( n, sort_bubble_up= True )

            g = self.tree.get_graph( )
            file_name = os.path.join( self.dir, 'ut02_g02' )
            self.tree.save_graph( file_name = file_name )
        except Exception as e:
            print( 'test_02(), error: {}'.format( e ) )


    def test_03(self):
        try:
            print( 'extract the smallest value, root node.' )
            n = self.tree.extract_min_value()
            print( 'root was smallest value: {}'.format( n.value ) )

            g = self.tree.get_graph( comment='smallest value removed' )
            file_name = os.path.join( self.dir, 'ut02_g03' )
            self.tree.save_graph( file_name = file_name )
        except Exception as e:
            print( 'test_03(), error: {}'.format( e ) )


    def __init__( self ):
        self.tree = MinHeapBinaryTree()

if __name__ == '__main__':
    t = Ut02()
    t.test_01()
    t.test_02()
    t.test_03()
    print( '... Unit Test end.' )
