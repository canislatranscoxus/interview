a = [
( 'zelda'   , 2 ),
( 'saweeti' , 6 ),
( 'ana'     , 3 ),
( 'saweeti' , 8 ),
( 'ana'     , 5 ),
( 'zelda'   , 4 ),
]

print ( '\n original list' )
print( a ) 

print( '\n sort by name and num of pets DESC' )
a2 = sorted( a, key = lambda t: ( t[0], t[1]), reverse = True   )
print( a2 )

import operator
s = sorted( a, key = operator.itemgetter( 0, 1 ) )
print( s )