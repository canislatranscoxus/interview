'''
description: Dynamic array
'''

class Dynamic_array:

    a            = None
    idx          = 0 # index of the last element of defined size.
    size         = 0
    grow_percent = 0.50 # from 0 to 1


    def append( self, obj ):
        if self.idx < self.size - 1:
            self.idx += 1
            self.a[ self.idx ] = obj
        else:
            self.idx  += 1
            grow_size  = int( self.size * self.grow_percent ) 
            grow_array = [ None ] * grow_size
            self.a.extend( grow_array )
            self.size = len( self.a )

            print( 'we are growing, my size is: {}'.format( self.size ) )




    def set_val( self, i, obj ):
        ''' set an object to our dynamic array at index i. '''
        if i > self.idx:
            return -1

        self.a[ i ] = obj
        return 0

    def __init__(self, size, grow_percent ):
        
        self.size         = size
        self.grow_percent = grow_percent
        self.idx          = size - 1
        self.a = [None] * size
        self.a[ 0 ] = 123
        print( self.a )


if __name__ == '__main__':
    
    print( '\n ... begin \n' )        

    # s = 5
    #g = 0.50
    s = 2
    g = 1.00
    a = Dynamic_array( size = s, grow_percent= g )

    for i in range( 0, s ):
        print( i )
        a.set_val( i, i )

    print( 'append and grow' )

    for i in range( s, 101 ):
        print( i )
        a.append( i )


    print( '\n ... end.' )        