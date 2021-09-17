print( '\n\n' )

a = [ 1,1,1, 2, 2, 3, 3, 3 ]
s = set( a )
print( 'set from array : {}'.format( s ) )

t1 = (10, 11)
t2 = (20, 22)

s.add( t1 )
s.add( t2 )
print( 'append tuples to set: {}'.format(s) )

s2 = set( t1 )
print( 'create set from tuple: {}'.format( s2 ) )

print( '{:>14,}'.format( 1234567890 ) )

