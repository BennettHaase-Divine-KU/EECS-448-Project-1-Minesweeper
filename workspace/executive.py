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
        self.gameBoard.print_board()
        self.gameBoard.place_bomb()
        self.gameBoard.print_board()

        self.gameState=0 #gameState 0->unresolved, 1->Win, 2->Loose
        while self.gameState==0:
        #Main Game Loop
            self.gameState=1
            continue
        return


