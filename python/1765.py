from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(isWater), len(isWater[0]) # sizes
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] # down, right, up, left
        heights = [[-1] * COL for _ in range(ROW)] # empty array w/ same size
        # heights = [[100] * COL for _ in range(ROW)] # empty array w/ same size
        cells = deque()

        def bfs(i, j):
            while len(cells) > 0:
                print("BFS iteration")
                i, j = cells.popleft()
                val = heights[i][j]
                for di, dj in dirs:
                    if (min(i+di, j+dj) < 0 or # OOB↓
                        i+di >= ROW or j+dj >= COL or # OOB↑
                        isWater[i+di][j+dj] == 1 or # water
                        heights[i+di][j+dj] != -1 and # visited # WRONG
                        heights[i+di][j+dj] <= val+1 # visited
                        ):
                        continue
                    else:
                        heights[i+di][j+dj] = val + 1
                        cells.append((i+di, j+dj))
            print(heights)
            pass

        # initialize BFS on *all* water cells
        for i in range(ROW):
            for j in range(COL):
                if isWater[i][j] == 1:
                    print("initiated BFS")
                    heights[i][j] = 0
                    cells.append((i, j))
                    bfs(i, j)

        return heights


# Test cases to validate the solution
def test_highestPeak():
    test_cases = [
        # Example 1
        {
            "input": [[0,1],[0,0]],
            "expected": [[1,0],[2,1]]
        },
        # Example 2
        {
            "input": [[0,0,1],[1,0,0],[0,0,0]],
            "expected": [[1,1,0],[0,1,1],[1,2,2]]
        },
        # All water cells
        {
            "input": [[1,1],[1,1]],
            "expected": [[0,0],[0,0]]
        },
        # No water cells (should not happen in valid input)
        {
            "input": [[0,0],[0,0]],
            "expected": [[-1,-1],[-1,-1]]
        }
    ]


    sol = Solution()
    for idx, test in enumerate(test_cases):
        result = sol.highestPeak(test["input"])
        assert result == test["expected"], f"Test case {idx + 1} failed: expected {test['expected']}, got {result}"
        print(f"Test case {idx + 1} passed")

# Run the tests
if __name__ == "__main__":
    test_highestPeak()
