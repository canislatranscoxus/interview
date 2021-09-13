'''
Question    : 1.5 One way

description : Given two strings, write a function to check 
              if they are one edit ( or zero edits ) away.

example     :

    pale , ple  ---> true
    pales, pale ---> true
    pale , bale ---> true
    pale , bake ---> false

'''

def is_one_char_dif( s1, s2 ):
    # s1 and s2 must be of the same size
    num_edits = 0
    for i in range( 0, len( s1 ) ):
        if s1[ i ] != s2[ i ]:
            num_edits += 1

    return num_edits <= 1

def is_missing_one_char( small, big ):
    num_edits   = 0
    i_small     = 0
    i_big       = 0
    while num_edits <=1 and i_small < len( small ) :
        if small[ i_small ] != big[ i_big ]:
            num_edits   += 1
            i_big       += 1
        else:
            i_small     += 1
            i_big       += 1

    return num_edits <= 1


def one_way( s1, s2 ):
    size_dif = abs( len( s1 ) - len( s2 ) )
    if size_dif > 1:
        return False
    
    small = s1
    big   = s2
    if len( s2 ) < len( s1 ):
        small = s2
        big   = s1
    
    if size_dif == 1:
        return is_missing_one_char( small, big )
    else:
        return is_one_char_dif( small, big )

if __name__ == '__main__':
    #s1, s2 = 'pale' , 'ple'  # True
    #s1, s2 = 'pales', 'pale' # True
    #s1, s2 = 'pale' , 'bale' # True
    #s1, s2 = 'pale' , 'bake' # False
    s1, s2 = 'acd', 'abcd' # True


    print( '"{}" \t "{}"'.format( s1, s2 ) )
    if one_way( s1, s2 ):
        print( 'YES, they are one way ... or another' )
    else:
        print( 'NO, they are not one way' )