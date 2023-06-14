
class Term:
    coeficient  = 0
    exponent    = 0

    def __init__( self, coeficient, exponent):
        self.coeficient  = coeficient
        self.exponent    = exponent


    def __add__( self, term ):
        if self.exponent == term.exponent:
            t = Term(self.coeficient + term.coeficient, self.exponent)
            return t

        return None

class Expression:
    terms = None

    def add_update( self, term ):
        self.terms[ term.exponent ] = term

    def show( self ):
        for k, t in self.terms.items():
            print( '{} x ^ {}'.format( t.coeficient, t.exponent ) )

    def __add__( self, exp2 ):
        expr3 = Expression()

        # insert all the terms from this object
        for exponent, t1 in self.terms.items():
            if exponent in exp2.terms:
                t2 = exp2.terms[ exponent ]
                t3 = t1 + t2
                expr3.add_update( t3 )
                exp2.terms.pop( exponent )
            else:
                expr3.add_update( t1 )

        # insert terms from exp2 that do not exist in this object.
        for exponent, t2 in exp2.terms.items():
            expr3.add_update( t2 )

        return expr3

    def __init__(self):
        self.terms = dict()


if __name__ == '__main__':
    '''t1 = Term( 2, 3 )
    t2 = Term( 7, 3 )    
    t3 = t1 + t2
    print( 't3 {} '.format( t3 ) )'''


    exp1 = Expression()
    exp2 = Expression()
    for i in range( 1, 5):
        t1 = Term( i * 2, i )
        t2 = Term( i * 3, i )    
        exp1.add_update( t1 )
        exp2.add_update( t2 )



    print( '\n exp1 ' )
    exp1.show()
    
    print( '\n exp2 ' )
    t2 = Term( 66, 6 )    
    exp2.add_update( t2 )
    t2 = Term( 77, 7 )   
    exp2.add_update( t2 ) 
    exp2.show()

    print( '\n result \n' )
    exp3 = exp1 + exp2
    exp3.show()
    