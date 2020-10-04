'''
description: write a function that receive as input an integer and return as output
                the name of the spreadsheet column. example:

                 input       output
                -------     --------
                    1            A
                    2            B
                    3            C
                    ...
                    26           Z
                    27          AA
                    28          AB
                    52          AZ

                    702         ZZ
                    703         AAA
'''

def get_col_chr( n ):
    c = chr( 64 + n )
    #print( 'char: {}'.format( c ) )
    return c

def get_col_name( n ):
    base = 26
    column_name = ''

    # build the column name
    while ( n > 0 ):
        r = n % base
        n = n // base

        if r == 0:
            column_name = 'Z' + column_name
            n -= 1
        else:
            c = get_col_chr( r )
            column_name = c + column_name


    print( 'column_name: {}'.format( column_name ) )
    return  column_name

get_col_name( 702 )




