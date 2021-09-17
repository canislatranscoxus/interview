'''
Find the positive integers from 0 to 100 for

  3    3     3   3
 a  + b   = c + d


My reasoning is, in the X axis



a    c    d     b
|    |    |     |       
----------------------->

Complexity = O ( n^4 )
This is brute force. Real bad performance. see other solutions.

'''
n = 3
ab = 0
cd = 0


for b in range(3, 100):
    for a in range( 0, b-2):
    
        ab = a**n + b**n
        for d in range( a+2, b ):
            for c in range( a+1, d ):
                cd = c**n + d**n
                if ab == cd:
                    print( 'a:{}; b:{}; c:{}; d:{}; ab:{}; cd:{}'.format( a, b, c, d, ab, cd)  )
                elif cd > ab:
                    break;


