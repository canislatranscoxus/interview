'''
question 1.7 Matrix Rotation

strategy 1. see the matrix as multiple onion rings or layers. First rotate the external ring, 
            then continue with the next, so the last ring will be the most internal, 
            the one who is in the center. 

'''

class SpinMatrix:

    # size is n x n. n is number of rows and columns.
    n = 0
    m = []


    def rotate_4_boxes( self, r, i ):
        z                = self.n - r -1
        tmp              = self.m[ r + i ][ z ]
        self.m[ r +i ][ z ] = self.m[ z ][ z - i ]
        self.m[ z ][ z - i ] = self.m[ z - i  ][ r ]
        self.m[ z -i ][ r ] = self.m[ r ][ r + i]
        self.m[ r   ][ r + i ] = tmp


    def rotate_ring( self, ring ):
        for i in range( ring, self.n - ring -1):
            self.rotate_4_boxes( ring, i )
    
    def rotate( self ):
        num_rings = self.n // 2
        for i in range( 0, num_rings ):
            self.rotate_ring( i )
            
    def _print( self ):
        #print( '\n ' )
        for row in range( 0, self.n ):
            for col in range( 0, self.n ):
                print( '\t{}'.format( self.m[ row ][ col ] ), end=""  )
            print( " ", end='\n' )


    def create_matrix(self, n):
        m = []
        i = 65
        for row in range( 0, n ):
            a = []
            for col in range( 0, n ):
                a.append( chr( i ) )
                i += 1
            
            m.append( a )
        return m


    def __init__(self, n ):
        self.n = n
        self.m = self.create_matrix( n )        


if __name__ == '__main__':
    m = SpinMatrix( 5 )
    print( '\n original matrix' )
    m._print(  )
    
    m.rotate()
    print( '\n rotated matrix' )
    m._print(  )

    print( '\n ... end test.' )