def findLongestPath(matrix):
    if not matrix or not matrix[0]:
        return 0  # Handle empty matrix case
    
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Movement directions
    
    def dfs(i, j, start_height, visited):
        max_length = 1  # Path starts with current cell
        current_height = matrix[i][j]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj  # Neighbor cell
            
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
                next_height = matrix[ni][nj]
                # Move allowed if next height is not higher than current or start
                if (next_height <= current_height) or (next_height <= start_height):
                    visited.add((ni, nj))  # Mark as visited
                    length = 1 + dfs(ni, nj, start_height, visited)
                    max_length = max(max_length, length)
                    visited.remove((ni, nj))  # Backtrack
        
        return max_length
    
    max_path = 0  # Track longest path
    
    for i in range(rows):
        for j in range(cols):
            visited = {(i, j)}  # Start DFS from each cell
            max_path = max(max_path, dfs(i, j, matrix[i][j], visited) - 1)
    
    return max_path  # Return final result

# Sample input
matrix = [
    [7, 8, 3],
    [5, 2, 4],
    [6, 3, 1]
]

# Test the function
result = findLongestPath(matrix)
print(result)  # Expected output: 7
