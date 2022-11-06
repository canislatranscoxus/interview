'''
Question 1.8 Zero Matrix.

Write an algorithm such that if an element in a M x N matrix is 0,
its entire row and column are set to 0.


'''

class ZeroMatrix:

    matrix = []
    rows = 0
    cols = 0

    def get_zpoints( self  ):
        a = []
        for r in range( 0, self.rows ):
            for c in range( 0, self.cols ):
                if self.matrix[ r ][ c ] == 0:
                    a.append( ( r, c ) )
        return a


    def clean( self, row, col ):
        # clean row
        for c in range( 0, self.cols ):
            self.matrix[ row ][ c ] = 0

        # clean column
        for r in range( 0, self.rows ):
            self.matrix[ r ][ col ] = 0


    def _print( self ):

        print( '\n' )
        for r in range( 0, self.rows ):
            for c in range( 0, self.cols ):
                print( '\t{}'.format( self.matrix[r][c] ), end='' )
            print( ' ', end='\n' )

    def run( self ):
        zpoints = self.get_zpoints()
        for point in zpoints:
            self.clean( point[ 0 ], point[ 1 ] )


    def __init__( self, matrix, m, n ):
        self.rows = m
        self.cols = n
        self.matrix = matrix


if __name__ == '__main__':

    m = 4
    n = 3
    matrix = [
        [  1,  2,  3 ],
        [  0,  5,  6 ],
        [  7,  0,  9 ],
        [ 10, 11, 12 ],                
    ]

    z = ZeroMatrix( matrix, m, n )
    print( '\n original matrix \n' )
    z._print()
    z.run()

    print( '\n zero matrix' )
    z._print()

    print( '... end.' )