# GoogleInterview
🧩 **_Matrix Jump Path Problem_**
**Problem Statement**
Given a 2D matrix where each cell represents a height, find the longest valid jumping path.
From any cell, you can jump to adjacent cells (up, down, left, right) based on the following rules:
* You can jump from cell A to adjacent cell B if height(B) <= height(A).
* You can continue jumping to cell C from B only if:
  -> height(C) <= height(B) (continue going down), or
  -> height(C) <= height(A) (can "bounce" back up, but not above the original height A).
* Each cell can be visited only once per path.

Goal: Find the longest valid jumping path in terms of number of steps (not the number of cells).

**Sample Input**:  
7 8 3  
5 2 4  
6 3 1

**Sample Output**:
7 

**Explanation**:
One possible optimal path:
8 → 7 → 5 → 2 → 4 → 1 → 3
Total jumps = 7 steps
-------------------------------------------------------------------------------------------------------------------------------------
  🧠 **Approach**
      We use Depth-First Search (DFS) to explore all valid jumping paths from each cell in the matrix.

  🔍 **Core Logic:**
      -> Start DFS from every cell in the matrix.
      -> At each step, we explore all 4 directions (up, down, left, right).
      -> We move to a neighbor cell if:
          -> Its height is less than or equal to the current cell, or
          -> Its height is less than or equal to the original start cell (to allow "bounce-back" jumps without exceeding the original height).
      -> We keep track of visited cells to avoid cycles.
      -> For each starting point, we calculate the maximum path length and update the overall maximum. 

  ⏱ **Time Complexity:**
      O(m × n × 4^k) — DFS from each cell, exploring up to 4 directions for up to k steps (longest path length). No memoization.

  🗂 **Space Complexity:**
    O(k) — Due to recursion and visited set during DFS, where k is the max path length.
