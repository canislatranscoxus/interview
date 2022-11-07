'''
Cracking the Coding Interview. 
Gayle Laakmann Mcdowell.
6th edition.

Chapter 3. Stacks and Queues.
pag 99

problem 3.5. : Write a program to sort a stack such that the smallest item are on the top.
You can use an additional temporal stack, but you may not copy the elements into any other 
data structure ( such as an array ). The stack support the following operations: 
push, pop, peek and isEmpty.

Peek() is one of a stack operation that returns 
the value of the top most element of the stack 
without deleting that element from the stack.

'''

class MyStack:

    # stack
    s = [] # stack


    def push( self, n ):
        self.s.append( n )


    def pop( self ):
        result = self.s.pop()
        return result


    def peek( self ):
        if len( self.s ) == 0:
            return None

        result = self.s[ -1 ]
        return result

    def sort( self ):
        _max    = None # Maximum value
        n_times = None

        if len( self.s ) == 0:
            return

        while True:
            self.set_max( _max, n_times )




    
    def set_max( s, _max, n_times ):
        
        tmp = [] # temporal stack

        # move elements from s to tmp stack

        # get _max and n_times

        # push _max to s stack

        # move elements from tmp to s stack.


