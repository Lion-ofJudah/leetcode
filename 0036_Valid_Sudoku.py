class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        i = 0
        while i < len(board):
            row = board[i]
            d = set()
            for cell in row:
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
            del(d)
            i += 1

        for i in range(len(board)):
            d = set()
            for j in range(len(board)):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
            del(d)
        
        d = set()
        for i in range(3):
            for j in range(3):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(3):
            for j in range(3, 6):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(3):
            for j in range(6, len(board)):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        
        del(d)
        d = set()
        for i in range(3, 6):
            for j in range(3):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(3, 6):
            for j in range(3, 6):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(3, 6):
            for j in range(6, len(board)):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(6, len(board)):
            for j in range(3):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(6, len(board)):
            for j in range(3, 6):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)
        del(d)
        d = set()
        for i in range(6, len(board)):
            for j in range(6, len(board)):
                cell = board[j][i]
                if cell == ".":
                    continue
                else:
                    if cell in d:
                        return False
                    d.add(cell)

        return True

