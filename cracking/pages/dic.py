

d = dict()
d[ 'a' ] = 'ant'
d[ 'h' ] = 'hornet'
d[ 'c' ] = 'centipod'

d.pop( 'a' )

for k,v in d.items():
    print( '{}, {}'.format( k, v ) )
