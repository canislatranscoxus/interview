'''
question: 1.4 Palindrome Permutation:

Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same fordwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
You can ignore casing and non-letter characters.

strategy 1. O( n + d )  n = string size. d = dictionary size. d <= n
            O( 2n ) --> O( n )

            Used here. Use a dictionary and count the number of times 
            each character appears in the string. A palindrome permutation must have at must
            one char odd number of times.

strategy 2. O( n )
            Use an array instead of dictionary. This approach works well if always
            we are going to have a small code like ascii code and have just alphabeth letters.
            If we need unicode its better strategy 1.

strategy 3. O( n )
            Use a bit array. Use less space than strategy 2.            

'''

class P1_4:
    def clean( self, s ):
        s = s.upper( )
        #take only letters from A to Z.

        a = []
        for ch in s:
            if ord( ch ) >= 65 and ord( ch ) <= 90:
                a.append( ch ) 

        s2 = "".join( a )
        return s2

    
    def count_chars(self, s ):
        # count the frequency of each character
        d = {}

        for ch in s:
            if ch in d:
                d[ ch ] = d[ ch ] + 1
            else:
                d[ ch ] = 1

        return d

    def is_palindrome_permutation(self, d):
        # a palindrome can have at must 1 character that appear an odd number of times in the string.
        odds = 0

        for k,p in d.items ():
            if p % 2 == 1:
                odds += 1

        return odds <= 1

    def run( self, s ):
        s = self.clean( s )
        d = self.count_chars( s )
        flag = self.is_palindrome_permutation( d )
        

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
    s = 'abczyabc'
    p.run( s )