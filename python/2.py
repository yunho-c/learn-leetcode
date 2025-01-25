# https://leetcode.com/problems/add-two-numbers
# PARTIAL PASS

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# helpers
def li_to_ll(list: List[int]):
    """
    Helper function to convert a list to a linked list
    """
    head = ListNode(list[0])
    current = head
    for i in range(1, len(list)):
        current.next = ListNode(list[i])
        current = current.next
    return head

def ll_to_li(head: ListNode):
    """
    Helper function to convert a linked list to a list
    """
    list = []
    while head:
        list.append(head.val)
        head = head.next
    return list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list, new_digit = ListNode(), 0
        initial_head = new_list
        while l1 or l2: #
            # v1, v2 = l1.val, l2.val
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            new_val = v1 + v2 + new_digit
            if new_val >= 10:
                # print("triggered")
                new_digit = 1
                new_val %= 10
            else:
                new_digit = 0
            new_list.val = new_val
            if new_digit == 1:
                new_list.next = ListNode(new_digit)
            else:
                new_list.next = ListNode()
            # new_list.next = ListNode()
            prev_list = new_list
            new_list = new_list.next
            # l1 = l1.next
            # l2 = l2.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if prev_list.next.val == 0: # removing leading 0
            prev_list.next = None

        return initial_head


def test():
    cases = [
        # Example 1
        {
            "input": {"l1": [2, 4, 3], "l2": [5, 6, 4]},
            "expected": [7, 0, 8]
        },
        # Example 2
        {
            "input": {"l1": [0], "l2": [0]},
            "expected": [0]
        },
        # Example 3
        {
            "input": {"l1": [9, 9, 9, 9, 9, 9, 9], "l2": [9, 9, 9, 9]},
            "expected": [8, 9, 9, 9, 0, 0, 0, 1]
        },
    ]


    sol = Solution()
    for idx, test in enumerate(cases):
        result = sol.addTwoNumbers(li_to_ll(test["input"]["l1"]), li_to_ll(test["input"]["l2"]))
        assert ll_to_li(result) == test["expected"], f"Test case {idx + 1} failed: expected {test['expected']}, got {ll_to_li(result)}"
        print(f"Test case {idx + 1} passed")

# Run the tests
if __name__ == "__main__":
    test()

