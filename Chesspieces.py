import pygame

class Chesspiece():
    def __init__(self,color):
        self.color=color
        self.directions=None


    def get_moves(self,board,position):
        #This is used for rook, bishop and queen, the others must implement their own
        moves=[]
        for direction in self.directions:
            moves_temp=self.get_moves_in_direction(board,position,direction)
            for i in moves_temp:
                moves.append(i)
                
        return moves

    def get_moves_in_direction(self, board, position, direction):
        moves = []
        print(position[0])
        i = position[0]+direction[0]
        j = position[1]+direction[1]
        while self.inbounds(i, j) and not board[i][j]:
            moves.append((i, j))
            i += direction[0]
            j+= direction[1]
        if self.inbounds(i, j) and board[i][j]:
            if self.color != board[i][j].color:
                moves.append((i, j))

        return moves

    
    def inbounds(self,i,j):
        return i<8 and i>=0 and j<8 and j>=0

class Pawn(Chesspiece):
    def __init__(self,color):
        self.ID="P"
        self.moved = False
        self.color=color

    def get_moves(self,board,position):
        moves=[]
        print(position)
        direction = -1 if self.color == "W" else 1
        if not board[position[0]][position[1]+direction]:
            moves.append((position[0], position[1]+direction))

        if not (self.moved and board[position[0]][position[1]+2*direction]):
            moves.append((position[0], position[1]+2*direction))

        if self.inbounds(position[0]-1,position[1]+direction) and board[position[0]-1][position[1]+direction] and board[position[0]-1][position[1]+direction].color != self.color:
            moves.append((position[0]-1, position[1]+direction))

        if self.inbounds(position[0]+1,position[1]+direction) and board[position[0]+1][position[1]+direction] and board[position[0]+1][position[1]+direction].color != self.color:
            moves.append((position[0]+1, position[1]+direction))
        return moves


class Rook(Chesspiece):
    def __init__(self,color):
        super().__init__(color)
        self.ID="R"
        self.directions=[(1,0),(0,1),(-1,0),(0,-1)]

class Bishop(Chesspiece):
    def __init__(self,color):
        super().__init__(color)
        self.ID="B"
        self.directions=[(1,1),(1,-1),(-1,1),(-1,-1)]

class Queen(Chesspiece):
    def __init__(self,color):
        super().__init__(color)
        self.ID="Q"
        self.directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

class Knight(Chesspiece):
    def __init__(self,color):
        super().__init__(color)
        self.ID="K"
        self.move_list=[(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]

    def get_moves(self,board,position):
        moves=[]
        for move in self.move_list:
            i=move[0]+position[0]
            j=move[1]+position[1]
            if self.inbounds(i,j) and (not board[i][j] or board[i][j].color!=self.color):
                moves.append((move[0]+position[0],move[1]+position[1]))
        return moves

class King(Chesspiece):
    def __init__(self,color):
        super().__init__(color)
        self.ID="Ki"
        self.move_list=[(1,0),(1,1),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

    def get_moves(self,board,position):
        moves=[]
        for move in self.move_list:
            i=move[0]+position[0]
            j=move[1]+position[1]
            if self.inbounds(i,j) and (not board[i][j] or board[i][j].color!=self.color):
                moves.append(move+position)
        
        return moves


    
        

    

