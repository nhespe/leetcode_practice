""" 371. Sum of Two Integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1"""

class Solution:
    def getSum_Slow(self, a: int, b: int) -> int:
        for i in range(abs(b)):
            if b < 0:
                a-=1
            else:
                a+=1
        return a

	def get_sum_fast(a: int, b: int) -> int: 
	    while (b != 0):
	        c = a & b  # Find the carry bits
	        a = a ^ b  # Add the bits without considering the carry
	        b = c << 1  # Propagate the carry
	    return a


print(add(45,2))


s = Solution()
print(s.getSum(-2,11))
print(s.getSum(2,-11))