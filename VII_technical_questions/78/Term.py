'''
Sum two expresions of the form: Ax^1 + bx^2 + bx^3 ...

'''

class Term:
    coeficient = 0
    exponent   = 0

    def __add__( self, term ):
        if self.exponent == term.expoenent:
            t = Term( self.coeficient + term.coeficient, self.exponent )
            return t
        return None

    def __init__( self, coeficient, exponent ) -> None:
        self.coeficient = coeficient
        self.exponent   = exponent
        

