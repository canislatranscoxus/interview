'''
question: 1.4 Palindrome Permutation:

Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same fordwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters.


strategy 3. O( n )
            Use a bit array. Use less space than strategy 2.            

'''

class P1_4:
    #num_letters = 90 - 65 + 1
    num_letters = 4


    def clean( self, s ):
        s = s.upper( )
        #take only letters from A to Z.

        a = []
        for ch in s:
            if ord( ch ) >= 65 and ord( ch ) <= 90:
                a.append( ch ) 

        s2 = "".join( a )
        return s2


    def toggle( self, a, index ):
        # works like a toggle electric switch to turn ON/OFF 
        mask = 1 << index
        a = a ^ mask
        return a


    def create_bit_array( self ):
        a = 1 << self.num_letters
        a = self.toggle( a, self.num_letters )
        return a


    def flag_odd_freq(self, s ):
        # count the frequency of each character

        a = self.create_bit_array()
        for ch in s:
            index = ord( ch ) -65
            a = self.toggle( a, index )

        return a

    def is_palindrome_permutation( self, a ):
        # a palindrome can have at must 1 character that appear an odd number of times in the string.
        
        mask        = a - 1
        bit_array   = a & mask
        return bit_array == 0


    def run( self, s ):
        s = self.clean( s )
        a = self.flag_odd_freq( s )
        flag = self.is_palindrome_permutation( a )
        

        print( 'string: "{}"'.format( s ) )
        if flag:
            print( 'Yes, it is a permutation of a Palindrome' )
        else:
            print( 'No, it is not a permutation of a Palindrome' )


if __name__ == '__main__':

    p = P1_4()
    #s = 'taco cato'
    #s = 'taco cat'
    #s = 'atco cta'
    #s = 'abczyabc'
    s = 'aabbccc'
    s = 'aabbcccddd'
    p.run( s )