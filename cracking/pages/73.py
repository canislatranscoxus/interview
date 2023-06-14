'''
Description. Page 73. Given two arrays a and b, find the elements 
             that exist in both arrays.

             This algorithm is runtime O( N )

'''

def intersected( a, b ):
    
    size_b  = len(b)
    i       = 0
    for obj in a:
        while i < size_b and b[ i ] <= obj :
            if obj == b[ i ]:
                print( obj )
            i = i + 1

if __name__ == '__main__':
    a = [ 13, 27, 35, 40, 49, 55, 59 ]
    b = [ 17, 35, 39, 40, 55, 58, 60 ]

    print( '\n\n... begin. \n\n' )
    intersected( a, b )
    print( '\n\n... end. \n\n' )

