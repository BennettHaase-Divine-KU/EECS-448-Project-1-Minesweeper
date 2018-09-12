from board import Board

class executive:
    def __init__(self, length, width, bombCnt):
        self.gameBoard=Board()
        self.length=length
        self.width=width
        self.bombCnt=bombCnt

    def checkWinLoose(self):
        return
    def setUpBoard(self):
        self.gameBoard.make_board(self.width, self.length, self.bombCnt)
        return
    def revealTile(self):
        return

    def run(self):
        self.setUpBoard()
        self.gameBoard.print_board_true()
        self.gameBoard.place_bomb()


        self.gameState=0 #gameState 0->unresolved, 1->Win, 2->Loose
        while self.gameState==0:
            self.gameBoard.print_board_true()
            self.gameBoard.print_board()

            #Main Game Loop
            print("Select a spot to reveal")
            print("x pos:")
            x=int(input())
            print("y pos:")
            y=int(input())

            self.gameState=self.gameBoard.reveal_tile(x,y)
            continue
        self.gameBoard.print_board()
        print("GAME OVER")
        return


