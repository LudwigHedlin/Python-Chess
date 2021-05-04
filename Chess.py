import pygame
import Chesspieces

class Chess():
    def __init__(self):
        pygame.init()
        self.running=True
        self.screen=pygame.display.set_mode((1000,800))
        pygame.display.set_caption("Chess")

        self.board = [[0 for x in range(8)] for x in range(8)]
        self.movehistory=[]
        self.captured_black=[]
        self.captured_white=[]
        self.available_moves=[]
        self.num_moves=0
        self.current_piece_index=None
        self.which_turn={0:"W",1:"B"}

        self.colors={"W":(200,200,200),"B":(40,40,40)}
        self.reset_board()


    def __del__(self):
        pygame.quit()

    def reset_board(self):
        self.num_moves=0
        self.available_moves=[]
        self.current_piece_index=None
        for i in range(8):
            self.board[i][1]=Chesspieces.Pawn("B")
            self.board[i][6] = Chesspieces.Pawn("W")
        
        self.board[0][0],self.board[7][0]=Chesspieces.Rook("B"),Chesspieces.Rook("B")
        self.board[0][7],self.board[7][7]=Chesspieces.Rook("W"),Chesspieces.Rook("W")

        self.board[1][0],self.board[6][0]=Chesspieces.Knight("B"),Chesspieces.Knight("B")
        self.board[1][7],self.board[6][7]=Chesspieces.Knight("W"),Chesspieces.Knight("W")

        self.board[2][0],self.board[5][0]=Chesspieces.Bishop("B"),Chesspieces.Bishop("B")
        self.board[2][7],self.board[5][7]=Chesspieces.Bishop("W"),Chesspieces.Bishop("W")

        self.board[3][0],self.board[4][0]=Chesspieces.King("B"),Chesspieces.Queen("B")
        self.board[3][7],self.board[4][7]=Chesspieces.King("W"),Chesspieces.Queen("W")

    def check_check(self,king_position,king_color):
        for i in range(8):
            for j in range(8):
                piece=self.board[i][j]
                if piece:
                    if king_color!=piece.color and king_position in piece.get_moves(self.board,(i,j)):
                        return True
        
        return False

    def promotion(self):
        pass

    def move(self,position):
        captured_piece = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]]=self.board[self.current_piece_index[0]][self.current_piece_index[1]]
        self.board[self.current_piece_index[0]][self.current_piece_index[1]]=0
        self.movehistory.append((self.current_piece_index,position,captured_piece))
        
        king_index=self.get_king(self.which_turn[self.num_moves%2])
        
        if self.check_check(king_index,self.which_turn[self.num_moves%2]):
            self.undo_move()
        
        self.num_moves+=1
        self.available_moves=[]
        self.current_piece_index=None

    def get_king(self,color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    if self.board[i][j].ID == "Ki" and self.board[i][j].color==color:
                        return (i,j)

    def undo_move(self):
        if self.num_moves>0:
            self.num_moves-=1
            last_move=self.movehistory.pop()
            last_piece=last_move[2]
            last_destination=last_move[1]
            last_position=last_move[0]
            self.board[last_position[0]][last_position[1]]=self.board[last_destination[0]][last_destination[1]]
            self.board[last_destination[0]][last_destination[1]]=last_piece
            
            self.available_moves=[]
            self.current_piece_index=None
        

    def get_available_moves(self,position):
        i=position[0]
        j=position[1]
        piece = self.board[i][j]
        if piece:
            self.available_moves=piece.get_moves(self.board,position)

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2==0:
                    self.draw_rect(i,j,(100,30,30))
                else:
                    self.draw_rect(i,j,(255,255,255))


    def draw_available_moves(self):
        for move in self.available_moves:
            self.draw_rect(move[0],move[1],(10,200,40,1))

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    piece = self.board[i][j]
                    self.draw_string(i,j,piece.ID,self.colors[piece.color])

    def draw_rect(self, i, j, color):
        rectangle = pygame.Rect(300+i*50, 150+j*50, 50, 50)
        pygame.draw.rect(self.screen, color, rectangle)

    def draw_string(self,i,j,string,color):
        font = pygame.font.SysFont('bold', 30)

        surface = font.render(string, 1, color)

        self.screen.blit(surface, (315+i*50, 165+j*50))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_board()
        self.draw_available_moves()
        self.draw_pieces()
        pygame.display.update()

    def get_index_from_pos(self,x,y):
        x=x-300
        y=y-150
        if x>=0 and y>=0:
            x=x//50
            y=y//50
            if x<8 and x>=0 and y<8 and y>=0:
                return (x,y)
        else:
            return False




def main():
    chess=Chess()
    chess.draw()
    
    while chess.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chess.running = False

            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                indexes=chess.get_index_from_pos(position[0],position[1])
                piece=chess.board[indexes[0]][indexes[1]]
                if piece and chess.which_turn[chess.num_moves%2]==piece.color:
                    chess.current_piece_index=indexes
                    chess.get_available_moves(indexes)
                if indexes in chess.available_moves:
                    chess.move(indexes)

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_z:
                    chess.undo_move()
                    
            
        chess.draw()


main()
