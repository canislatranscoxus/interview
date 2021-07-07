'''
description: my dynamic array

'''

class Dynamic_array():
    idx_last     = -1   # index of last element in the array
    grow_percent = 1.0 # from 0 to 1
    a            = None
    size         = 0

    def __init__( self, size, grow_percent = 1.0 ):
        self.size           = size
        self.grow_percent   = grow_percent 
        self.a              = [ None ] * size 
        self.idx_last       = -1

    def get_new_array( self ):
        new_size  = int ( self.size * ( 1 + self.grow_percent ) )
        new_array = [ None ] * new_size
        return new_array

    def append( self, obj ):
        if self.idx_last < self.size:
            self.idx_last           += 1
            self.a[ self.idx_last ]  = obj

        # if array is full, increase capacity
        if self.idx_last == self.size - 1:
            new_array = self.get_new_array(  )

            # copy data to new array
            for i in range( 0, len( self.a ) ):
                new_array[ i ] = self.a[ i ] 

            self.a      = new_array
            self.size   = len( new_array )

    def set( self, idx, obj ):
        if idx >= self.size:
            return -1

        self.a[ idx ] = obj
        return 0

def ut_01():
    size         = 2
    grow_percent = 1 # from 0 to 1. 
    a = Dynamic_array( size, grow_percent )

    a.append( 'dog' )
    a.append( 'cat' )
    a.append( 'fish' )
    a.append( 'bird' )
    a.append( 'turttle' )
    a.append( 'ant' )
    a.append( 'bee' )
    a.append( 'scorpion' )
    a.append( 'hornet' )
    a.append( 'spider' )

    print( 'size: {}'.format( a.size ) )
    for i in a.a:
        print( i )

if __name__ == '__main__':
    ut_01()