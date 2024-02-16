'''
Cracking the Coding Interview. 
Gayle Laakmann Mcdowell.
6th edition.
Chapter 3. Stacks and Queues.
pag 98

problem 3.2. Stack min:
How would you design a stack which, in addition to push and pop, has a function min 
which returns the minimum element? Push, pop, and min should all operate in O(1) time.

strategy:

Create a class with two stacks as attributes, 
    data stores numbers, 
    mins stores the min values. 
    
To get the min value we get the last value from mins.

in this way insert, pop and min always be O(1) because do not need to loop all the collection,
just insert, or pop in the last element of the stacks.

'''

class MyStack:
    data = []
    mins = []

    def __len__( self ):
        return len( self.data )

    def get_min( self ):
        if len( self.mins ) == 0:
            return None

        return self.mins[ -1 ]


    def insert( self, *numbers ):

        for n in numbers:
            self.data.append( n )

            if  len( self.mins ) == 0 or  n < self.mins[ -1 ]:
                self.mins.append( n )


    def pop( self ):

        if len( self.data ) == 0:
            return None

        result = self.data.pop()
        tmp_min = self.mins.pop()

        if len( self.data ) == 0 :
            return result

        if ( len( self.mins ) == 0 ) \
        or self.data[ -1 ] < self.mins[ -1 ]:
            self.mins.append( tmp_min )

        return result

s = MyStack()
s.insert( 10, 13, 12, 5, 8, 6, 7, 5, 5, 3 )



while len( s ) > 0:
    print( s.data )
    m = s.get_min()
    print( 'min: {} \n'.format( m ) )
    s.pop()

print( '\n end. \n' )    