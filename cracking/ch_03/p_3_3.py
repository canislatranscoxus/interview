'''
Cracking the Coding Interview. 
Gayle Laakmann Mcdowell.
6th edition.

Chapter 3. Stacks and Queues.
pag 99

problem 3.3. : Stack of Plates.

Imagine  a  (literal) stack  of  plates. If the stack gets to high, it may topple. Therefore,
in real life, we would like start  a new stack when the previous stack exeeds some threshold.
Implement  a data structure "SetOfStacks" that mimics this. SetOfStacks should be composed of
several stacks  and  should create  a  new  stack  once  the  previous  one  exeeds capacity.

SetOfStacks.push() and SetOfStacks.pop()should behave identically to a single stack ( that is,
pop should return the same values as it would if there were just a single stack ).

Follow up
Implement a function popAt( int index ) which performs a pop operation on a specific sub-stack.

strategy:
create a class with a list of stacks.


    stack n
    .
    .
    .
    stack 3
    stack 2
    stack 1

'''

class SetOfStacks:
    
    a = [] # list of stacks
    stack_max_size = 5

    def push ( self, n ):
        
        if len( self.a ) == 0 or len( self.a[ -1 ] ) == self.stack_max_size:
            # the list of stacks is empty or the last stack is full
            self.a.append( [ n ] )

        else:
            # we push to the last stack
            self.a[ -1 ].append( n )

    def pop  ( self ):
        # we pop from last stack

        result = None
        if len( self.a ) == 0:
            return result

        result = self.a[ -1 ].pop()
        return result


    def popAt( self, index ):
        # we pop from a specific location
        result = None

        if len( self.a ) == 0 or \
            index > len( self.a ):
            return result

        result = self.a[ index ].pop()
        return result



s = SetOfStacks()
n = 10
for stack in range( 0, 3 ):
    for i in range( 0, 5):
        s.push( n )
        n = n + 1

print( '\n set of stacks \n' )
for stack in range( 0, 3 ):

    print( 'stack: {}'.format( stack ) )
    for i in range( 0, 5):
        print( s.a[ stack ][ i ] )

s.popAt( 2 )
s.popAt( 0 )
s.popAt( 1 )
s.popAt( 0 )

s.pop()
s.pop()





print( '... end.' )


