class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        board_count = Counter(char for row in board for char in row)
        word_count = Counter(word)
        
        for char, freq in word_count.items():
            if board_count[char] < freq:
                return False
            
        visited = set()
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        rows = len(board)
        cols = len(board[0])
        
        def dfs(row,col,index):
            if index == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index] or (row,col) in visited:
                return False

            visited.add((row,col))
            for dr,dc in directions:
                new_r = dr+row
                new_c = dc+ col
                
                if dfs(new_r,new_c, index+1):
                    visited.remove((row,col))

                    return True
            visited.remove((row,col))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False 