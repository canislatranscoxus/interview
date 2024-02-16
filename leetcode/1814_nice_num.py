'''
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices.
Since that number can be too large, return it modulo 10 ^ 9 + 7.



Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:

Input: nums = [13,10,35,24,76]
Output: 4



Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 109
'''

class Solution:

    def rev(self, n):
        s = str( n )
        r =''
        for i in s:
            r =  i + r

        return int(r)

    def are_nice(self, i, j ):
        flag = False

        if i + self.rev(j) == self.rev(i) + j:
            flag = True

        return flag

    def ut_01(self):
        n = 12345
        reversed = self.rev( n )
        print('n       : {}'.format( n ) )
        print('reversed: {}'.format(reversed))
        assert reversed == 54321
        print( 'ut_01 ... OK' )

    def ut_02(self):
        flag = self.are_nice( 42, 97 )
        assert flag == True

        flag = self.are_nice(11, 1)
        assert flag == True

        print( '42 and 97 re nice, 11 and 1 are nice' )
        print( 'ut_02 ... OK' )

    def ut_03(self):
        nums = [42, 11, 1, 97]
        output = self.countNicePairs( nums )

        print( 'nums: {}'.format( nums ) )
        assert output == 2
        print( 'nums has 2 nice numbers' )
        print( 'ut_03 ... OK' )

    def countNicePairs(self, nums ) -> int:
        rev_nums = []
        num_of_pairs = 0

        # calculate the reversed of all the list nums.
        for i in nums:
            rev_nums.append( self.rev( i ) )

        # find all the nice numbers
        for i in range( 0, len(nums) -1 ) :
            for j in range( i + 1, len(nums)  ):
                #if self.are_nice( nums[ i ], nums[ j ] ):
                if nums[i] + rev_nums[ j ] == rev_nums[i] + nums[j]:
                    num_of_pairs += 1

        return num_of_pairs


# Unit Test
solution = Solution()
solution.ut_01()
solution.ut_02()
solution.ut_03()