"""20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

https://leetcode.com/problems/valid-parentheses/
"""
VALID_TOKENS = ["[", "]", "{", "}", "(", ")"]
COMPLIMENTS = {
    "{" : "}",
    "[" : "]",
    "(" : ")",
    ")" : "(",
    "}" : "{",
    "]" : "["
}

class Solution:
    def isValid(self, s):
        stack_start = [x for x in s if x in VALID_TOKENS]
        temp_stack = []
        if len(stack_start) % 2 != 0:
            return False

        while len(stack_start) > 0:
            temp_stack.append(stack_start.pop(-1))
            
            while temp_stack and stack_start and temp_stack[-1] == COMPLIMENTS[stack_start[-1]]:
                temp_stack.pop(-1)
                stack_start.pop(-1)

        if len(temp_stack) > 0:
            return False

        return True

x = Solution()
test = "{}"
print(x.isValid(test))












