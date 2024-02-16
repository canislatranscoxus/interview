'''
17_21. Volume of Histogram: imagine a histogram (bar graph).
        Design an algorithm to compute the volume of water
        it could hold if someone poured water across the top.
        You can assume that each histogram bas has widht 1.

EXAMPLE ( Black bars are the histogram. Gray is water )

input: { 0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0 }
output: 26

There are 3 boxes,

box 1, from col of heigh 4 to col of heigh 6, 4 x 3 = 12
box 2, from col of heigh 6 to col of heigh 5, 6 x 5 = 30
box 3, from col of heigh 5 to col of heigh 1, 2 x 1 =  2

Volume = 12 + 30 + 2 = 44
                 ╔═╗
                 ║ ║
                 ║ ║---------------------╔═╗
     ╔═╗---------║ ║                     ║ ║
     ║ ║         ║ ║         ╔═╗         ║ ║
     ║ ║         ║ ║         ║ ║         ║ ║
     ║ ║         ║ ║         ║ ║         ║ ║-----╔═╗
─────╚═╝─────────╚═╝─────────╚═╝─────────╚═╝─────╚═╝───────────
0  0  4   0   0   6   0   0   3   0   0   5   0   1   0   0   0


Hints: #628, #639, #650, #657, #661, #675, #692, #733, #741
'''

def get_first_bigger( i1, h ):
    # find the index of the first column bigger than the column of index i1
    for i in range( i1 + 1, len(h) ):
        if h[ i ] > h[ i1 ] :
            return i
    return None


def get_first_bigger_eq( i1, h ):
    # find the index of the first column bigger or equal than the column of index i1

    for i in range( i1 + 1, len(h) ):
        if h[ i ] >= h[ i1 ] :
            return i
    return None


def get_first_biggest( start, h ):
    max_col = max( h[ start: ] )

    for i in range( start, len( h ) ):
        if h[ i ] == max_col:
            return i
    return None

def find_boxes( h ):
    # find the big boxes that contain the rest of the boxes in the histogram.
    # We delimit a box from i1 to i2.
    # i1 = index of the column1 c1.
    # i2 = index of the column2 c2.
    #
    # To find the boxes there are 2 cases:
    #   case 0. c1 == 0
    #   case 1. c1 <= c2
    #   case 2. c1 >  c2.

    boxes = []
    i1 = 0
    i2 = 1
    while i2 < len( h ):
        c1 = h[ i1 ]
        a = h[ i1 + 1 : ]
        c2 = max( a )

        if c1 == 0:
            i1 = get_first_bigger( i1, h )
            i2 = i1 + 1
            continue

        if c1 <= c2:    # case 1. c1 <= c2
            i2 = get_first_bigger_eq( i1, h )

        else:           # case 2. c1 >  c2.
            i2 = get_first_biggest( i1 + 1, h )
            if h[ i2 ] == 0:
                break

        box     = ( i1, i2 )
        boxes.append( box )
        i1 = i2
        i2 = i2 + 1

    return boxes


def get_volumes( boxes, h ):
    # calculate the volume of each box.
    #
    # parameters:
    #   boxes = array of tuples. Each tuple has the indexes of start and end (i1 and i2 ).

    a = []
    for box in boxes:

        i1 = box[0]
        i2 = box[1]
        water_height = min( h[i1], h[i2] )
        box_vol = 0
        for i in range( i1 +1, i2 ):

            if h[i] >= water_height:
                continue

            col_vol =  water_height - h[i]
            box_vol = box_vol + col_vol

        if box_vol > 0:
            a.append( box_vol )

    return a



def get_volume_hist( h ):
    # Take as input a histogram, and
    # return as output the volume of the histogram
    #
    # parameters:
    #   h = array of int. Each element represent a column in the histogram.

    boxes     = find_boxes( h )
    boxes_vol = get_volumes( boxes, h )
    hist_vol  = sum( boxes_vol )
    return hist_vol


def main():
    #
    h = [ 0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
    v = get_volume_hist(h)
    print( 'histogram: {}'.format( h ) )
    print( 'volume: {}'.format( v ) )


main()
