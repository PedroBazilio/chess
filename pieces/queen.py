class Queen (Piece):
    
    def __init__(self):
        super.spriteDir = 'assets/img/' + super.color + 'Queen.png'

    def getPossibleMoves(self, coord, matrix):
        pass