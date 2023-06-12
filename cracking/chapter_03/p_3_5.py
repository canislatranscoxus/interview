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

    def isEmpty( self ):
        return len( self.s ) == 0
            

    def sort( self ):
        if len( self.s ) == 0:
            return

        i = 0
        while i < len( self.s ):
            i = self.sort_starting( self.s, i )


    
    def sort_starting( self, s, index ):
        
        tmp = [] # temporal stack

        _max = None
        times = 0

        # move elements from s to tmp stack
        # and find _max and times
        while len( s ) > index:
            n = s.pop()

            if _max == None or n > _max :
                _max  = n
                times = 1
            
            elif n == _max :
                times += 1

            tmp.append( n )


        # push _max to s stack
        for i in range(0, times ):
            s.append( _max )

        # get new index
        new_index = len( s )

        # move elements from tmp to s stack.
        while len( tmp ) > 0:
            n = tmp.pop()
            if n != _max:
                s.append( n )

        return new_index


# -----------------------------------------------------------------------------
# Unit Test
# -----------------------------------------------------------------------------

s = MyStack()

s.push( 10 )
s.push( 30 )
s.push( 20 )
s.push( 40 )


print( '\n original stack' )
print( s.s )

s.sort()
print( '\n sorted stack' )
print( s.s )

print( '\n ... end \n' )



