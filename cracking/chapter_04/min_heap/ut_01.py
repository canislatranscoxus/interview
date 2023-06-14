'''
Unit Test

Insert nodes:
    4, 50, 7, 55, 90, 87


the tree most be like this

            4
         /     \
      50        7
     /   \     /   \
   55    90   87   ⚪

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

dir = '/home/art/Downloads/'

a = [ 4, 50, 7, 55, 90, 87 ]

#a = [ 4 ]

tree = MinHeapBinaryTree()

for i in a:
    n = Node( i )
    tree.insert( n )

g = tree.get_graph( )

file_name = os.path.join( dir, 'ut01_g01' )
tree.save_graph( file_name = file_name )

n = Node( 2 )
tree.insert( n )

g = tree.get_graph( )
file_name = os.path.join( dir, 'ut01_g02' )
tree.save_graph( file_name = file_name )

print( 'Unit Test 01 ... end.' )