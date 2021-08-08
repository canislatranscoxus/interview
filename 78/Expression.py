'''
Sum two expresions of the form: Ax^1 + bx^2 + bx^3 ...

'''

class Expression:

    # dictionary. key is exponent, value is coeficient.
    terms = None


    def insert_term( self, t ):
        if t.exponent in self.terms:
            a_term = self.terms[ t.exponent ]
            t.coeficient += a_term.coeficient 

        self.terms[ t.exponent ] = t                

    def set_exp( self, list_of_terms ):
        for t in list_of_terms:
            self.insert_term( t )

    def __add__( self, exp2 ):
        expr3 = Expression()
        expr3.terms = self.terms.copy()
        for coeficient, t in exp2.terms.items():
            expr3.insert_term( t )
        return expr3

    def print2( self ):
        for coeficient, t in self.terms.items():
            print( ' {:+}x^({:+}) '.format( t.coeficient, t.exponent ), end= '' )
        
        print( '\n' )


    def clean( self ):
        self.terms.clear()
        self.terms = None

    def __init__( self ):
        self.terms = dict()
        print( 'constructor' )


