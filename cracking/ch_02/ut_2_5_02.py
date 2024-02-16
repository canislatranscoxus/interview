from p_2_5_02 import MyList

class Ut:

    def t_01( self ):
        '''Test sum reversed linked lists '''
        my_list = MyList()
        h1 = my_list.create_list_from_string( '716' )
        h2 = my_list.create_list_from_string( '592' )

        my_list._print( h1 )
        my_list._print( h2 )

        result = my_list.sum_reversed_lists( h1, h2 )
        s = my_list.to_str( result )
        i = my_list.to_int( result )
        my_list._print( result )

        assert s == '912'
        assert i == 912


    def t_02( self ):
        '''Test sum reversed linked lists '''
        my_list = MyList()
        h1 = my_list.create_list_from_string( '617' )
        h2 = my_list.create_list_from_string( '295' )

        my_list._print( h1 )
        my_list._print( h2 )

        result = my_list.sum_lists ( h1, h2 )
        s = my_list.to_str( result )
        i = my_list.to_int( result )
        my_list._print( result )

        assert s == '912'
        assert i == 912


if __name__ == '__main__':

    ut = Ut()
    ut.t_02()

