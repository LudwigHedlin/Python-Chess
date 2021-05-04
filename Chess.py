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

        self.colors={"W":(200,200,200),"B":(40,40,40)}
        self.reset_board()


    def __del__(self):
        pygame.quit()

    def reset_board(self):
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

    def check(self,king_position,king_color):
        pass

    def promotion(self):
        pass

    def get_available_moves(self,position):
        i=position[0]
        j=position[1]
        piece = self.board[i][j]
        if piece:
            self.available_moves=piece.get_moves(self.board,position)

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                print(i+j)
                if (i+j)%2==0:
                    self.draw_rect(i,j,(100,30,30))
                else:
                    self.draw_rect(i,j,(255,255,255))


    def draw_available_moves(self,position):
        for move in self.available_moves:
            self.draw_rect(move[1],move[0],(10,200,40))

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
        self.draw_available_moves
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
                if chess.board[indexes[0]][indexes[1]]:
                    chess.available_moves=chess.get_available_moves(indexes)
                    print(chess.available_moves)


main()
