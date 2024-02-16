start = 'A'
end   = 'E'
ch    = start
size = 1
s    = ''

while True:
    if size == 1:
        print( ch )
    else:
        print( ch + ' ' + ch * (size-1) )

    if ch == end:
        break

    ch = chr( ord( ch ) + 1 )
    size += 1

