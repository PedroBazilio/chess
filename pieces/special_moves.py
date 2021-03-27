from game_state import GameState
from utils import *
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn 
from pieces.queen import Queen
from pieces.rook import Rook
from copy import deepcopy

PIECES_EN = ['bishop', 'knight', 'pawn', 'queen', 'rook']
PIECES_PT = ['Bispo', 'Cavalo', 'Peão', 'Rainha', 'Torre']

class SpecialMoves:
    
    def __init__(self):
        self.selected_piece = None
    
    def en_passant(self, board, piece, row, col, ref):
        if (board.squares[(col+1, row)]['piece'] == GameState.possible_en_passant):
            board.pieceCapture((col+1, row))
        else:
            board.pieceCapture((col+1, row))

    def pawn_promotion(self, board, original_pawn, row, col, sprites):
        print("promocao")
        self.pawn_promotion_menu(board, original_pawn, row, col, sprites)
        
    def pawn_promotion_menu(self, board, original_pawn, row, col, sprites):
        listbox = tk.Listbox(board, selectmode = 'single', width = 7, height=6)
        listbox.pack(expand = True, fill = "both")
        label = tk.Label(board, text = "Selecione a peça na qual o peão se transformará")
        label.pack()
        for piece in PIECES_PT:
            listbox.insert(listbox.size(), piece)
        submit = tk.Button(master = board, text = "Escolher", command = lambda: self.destroy_promotion_menu(board, original_pawn, row, col, sprites))
        submit.pack()

    def destroy_promotion_menu(self, board, original_pawn, row, col, sprites):  
        self.selected_piece = PIECES_EN[board.children['!listbox'].curselection()[0]]
        # print(globals()['selected_piece'])
        board.children['!listbox'].destroy()
        board.children['!label'].destroy()
        board.children['!button'].destroy()
        self.set_piece(board, original_pawn, row, col, sprites)

    def set_piece(self, board, original_pawn, row, col, sprites): 
        print(self.__dict__)   
        print(self.selected_piece)
        piece_class = self.selected_piece.title()
        board.canvas.delete(original_pawn.name)
        del sprites[original_pawn.spriteID]
        player_color = original_pawn.color
        #piece_number 
        modified_pawn = deepcopy(original_pawn)
        modified_pawn = globals()[piece_class](player_color, player_color + '_' + self.selected_piece)
        modified_pawn.name += '_xxx'
        filename = player_color + (get_piece_type(modified_pawn.name)).title()
        modified_pawn.sprite_dir = 'assets/img/' + filename  + '.png'
        board.addPiece(modified_pawn, row, col)
        
    def castling(self):
        pass