""" Two Sum -> Q1
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

https://leetcode.com/problems/two-sum/

"""
from typing import List, Tuple

def find_indices(int_array: List[int], target: int) -> Tuple[int, int]:
	""" Compare each value against the other to find proper comparisons """
	for i in range(len(int_array)):
		for j in range(len(int_array) - (i + 1)):
			if int_array[i] + int_array[j + i + 1] == target:
				return i, j+i + 1

	return None, None

test_example_1 = [3,2,4], 6
test_example_2 = [1,2,3,4,5,6,6.5,6.6], 10
test_example_3 = [1,2,3,4,5,6,2,1], 2

print(find_indices(*test_example_1))
print(find_indices(*test_example_2))
print(find_indices(*test_example_3))
