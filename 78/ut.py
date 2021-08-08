
from Expression import Expression
from Term       import Term

def ut_01():
    e1 = Expression()
    e2 = Expression()

    a1 = [ Term( 10, 1 ), Term( -20, 2 ), Term( 30, -3 ) ]
    a2 = [ Term(  5, 1 ), Term(   6, 2 ), Term(  7, -3 ) ]

    e1.set_exp( a1 )
    e2.set_exp( a2 )

    e3 = e1 + e2
    e3.print2()


if __name__ == '__main__':
    ut_01()
    print( '...end.' )
