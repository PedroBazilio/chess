class Pawn (Piece):
    
    def __init__(self):
        super.spriteDir = 'assets/img/' + super.color + 'Pawn.png'

    def getPossibleMoves(self, coord, matrix):
        pass