# reverse a string

# Strategy 1
s = 'hello'
r = ''

print( 'original string: {}'.format( s ) )

for c in s:
    r = c + r
print( r )
print( '1. reversed : {}'.format( r ) )

# Strategy 2
r2 = ''
for i in range( len(s)-1, -1, -1 ):
    r2 = r2 + s[i]
print( '2. reversed : {}'.format( r2 ) )

