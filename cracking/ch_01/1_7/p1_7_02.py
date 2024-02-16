'''
question 1.7 Matrix Rotation

strategy 1. see the matrix as multiple onion rings or layers. First rotate the external ring, 
            then continue with the next, so the last ring will be the most internal, 
            the one who is in the center. 

SpinMatrix class rotate a matrix in any of two directions:
            clockwise
            anticlock_wise

┌─┐  
└─┘  


'''
class Rotation:
    CLOCKWISE       = 0
    ANTI_CLOCKWISE  = 1

class SpinMatrix:
    


    # size is n x n. n is number of rows and columns.
    n = 0
    m = []
    rotation = Rotation.ANTI_CLOCKWISE



    def rotate_4boxes_clockwise( self, r, i ):
        ''' roate 4 boxes clockwise, of ring r'''
        z                       = self.n - r -1
        tmp                     = self.m[ r + i ][ z ] # ┐
        self.m[ r + i ][ z     ] = self.m[ r    ][ r + i ] # ┐
        self.m[ r     ][ r + i ] = self.m[ z - i][ r     ] # ┌
        self.m[ z - i ][ r     ] = self.m[ z    ][ z - i ] # └
        self.m[ z     ][ z - i ] = tmp                     # ┘


    def rotate_4boxes_anti_clockwise( self, r, i ):
        ''' roate 4 boxes anti_clockwise, of ring r'''
        z                       = self.n - r -1
        tmp                     = self.m[ r + i ][ z     ] # ┐
        self.m[ r +i ][ z     ] = self.m[ z     ][ z - i ] # ┐
        self.m[ z    ][ z - i ] = self.m[ z - i ][ r     ] # ┘
        self.m[ z -i ][ r     ] = self.m[ r     ][ r + i ] # └
        self.m[ r    ][ r + i ] = tmp                      # ┌


    def rotate_ring( self, ring ):
        ''' rotate just one ring'''

        if self.rotation == Rotation.CLOCKWISE:
            f = self.rotate_4boxes_clockwise
        else:
            f = self.rotate_4boxes_anti_clockwise

        for i in range( ring, self.n - ring -1):
            f( ring, i )
    
    def rotate( self, rotation ):
        ''' rotate the entire matrix '''

        self.rotation = rotation
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

    for i in range(0, 4):
        m.rotate( Rotation.ANTI_CLOCKWISE )
        print( '\n rotated matrix' )
        m._print(  )

    print( '\n ... end test.' )