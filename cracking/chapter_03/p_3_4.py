'''
Cracking the Coding Interview. 
Gayle Laakmann Mcdowell.
6th edition.

Chapter 3. Stacks and Queues.
pag 99

problem 3.4. : Queue by Stacks.
Implement a MyQueue class which implements a queue using two stacks.
'''

class MyQueue:

    stack1 = []
    stack2 = []

    def push( self, n ):
        self.stack1.append( n )


    def pop( self ):
        result = None

        if len( self.stack1 ) == 0:
            return None

        while len( self.stack1 ) > 1:
            self.stack2.append( self.stack1.pop() ) 
        
        result = self.stack1.pop()

        while len( self.stack2 ) > 0:
            self.stack1.append( self.stack2.pop() ) 

        return result

    def pprint( self ):
        print( 'myQueue elements: ' )
        for i in self.stack1:
            print( i )

# -----------------------------------------------------------------------------
# Unit Test
# -----------------------------------------------------------------------------

myQueue = MyQueue()

myQueue.push( 'a' )
myQueue.push( 'b' )
myQueue.push( 'c' )
myQueue.push( 'd' )
myQueue.push( 'e' )

print( myQueue.pop() )
print( myQueue.pop() )

myQueue.pprint()

