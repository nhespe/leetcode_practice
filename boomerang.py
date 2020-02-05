""" 1037. Valid Boomerang
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100

https://leetcode.com/problems/valid-boomerang/
"""
from typing import List
import math

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        area =  (
			(points[0][0] * (points[1][1]-points[2][1])) +
			(points[1][0] * (points[2][1]-points[0][1])) +
			(points[2][0] * (points[0][1]-points[1][1]))
	    ) / 2.0

        return abs(area) > 0
   		

test1 = [[0,1], [0,2],[1,2]] # True
test2 = [[1,1], [2,1],[2,2]] # T
test3 = [[1,1], [0,1],[1,1]] # F
test4 = [[0,0],[1,0],[2,2]] # T
test5 = [[0,1],[1,1],[2,1]] # F

x = Solution()
print(x.isBoomerang(test1))
print(x.isBoomerang(test2))
print(x.isBoomerang(test3))
print(x.isBoomerang(test4))
print(x.isBoomerang(test5))