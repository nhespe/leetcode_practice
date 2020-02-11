"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  temp = 4->5,
  1 -> 1 ->

  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6"""
from typing import List
import copy

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """ Main Function: Taking list of head nodes """
        base_list = lists[0]

        for lst in lists[1:]:
            base_list = self.merge_two_lists(base_list, lst)

        return base_list


    def merge_two_lists(self, lst1, lst2):
        """ Merges two singly linked lists [Assumed individually sorted """
        return_pointer = lst1
        while lst1.next:
            while lst2 and lst1.val <= lst2.val:
                if lst1.next and lst1.next.val <= lst2.val or not lst1.next:
                    break
                temp_node = lst1.next
                lst1.next = copy.copy(lst2)
                lst2 = lst2.next
                lst1.next.next = temp_node

            lst1 = lst1.next
        
        if lst2:
            lst1.next = lst2
        
        self.printlist(return_pointer)
        return return_pointer


    def printlist(self, list1):
        """ Helped function to print lists """
        while list1:
            print(list1.val, sep=" ")
            list1 = list1.next
        print("end list")

    def make_list(self, listi):
        """ Helper function to make a linked list from list of ints """
        node_list = [ListNode(i) for i in listi]
        return_list = node_list[0]
        temp_node = node_list[0]
        for node in node_list[1:]:
            temp_node.next = node
            temp_node = temp_node.next
        self.printlist(return_list)
        return return_list

x = Solution()

list1 = x.make_list([1,4,5])
list2 = x.make_list([1,3,4])
list3 = x.make_list([2,6])
print(x.mergeKLists([list1, list2, list3]))













