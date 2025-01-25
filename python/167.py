# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# PASS

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            val = numbers[l] + numbers[r]
            if val < target:
                l += 1
            elif target < val:
                r -= 1
            elif val == target:
                return [l + 1, r + 1]
            elif l == r:
                break # did not find a match
        return -1 # not needed

def test():
    cases = [
        # Example 1
        {
            "input": {"numbers": [2,7,11,15], "target": 9},
            "expected": [1, 2]
        },
        # Example 2
        {
            "input": {"numbers": [2,3,4], "target": 6},
            "expected": [1, 3]
        },
        # Example 3
        {
            "input": {"numbers": [-1,0], "target": -1},
            "expected": [1, 2]
        },
    ]

    sol = Solution()
    for idx, test in enumerate(cases):
        result = sol.twoSum(test["input"]["numbers"], test["input"]["target"])
        assert result == test["expected"], f"Test case {idx + 1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {idx + 1} passed")

# Run the tests
if __name__ == "__main__":
    test()
