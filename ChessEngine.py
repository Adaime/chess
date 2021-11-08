"""
stores all information about the cuerrent state of chess game. Also be responsible for determining valid moves. It will also keep a move log.
"""

class GameState():
    def __init__(self):
        # 8 x 8 chess board
        # first character represents color of piece, 'b' (black) or 'w' (white)
        # second character represents type of piece, 'K', 'Q', 'R', 'B', 'N', or 'P'
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.moveLog = []
    
    '''
    Take a move as a parameter and executes it (this will not work for castling, en-passsant & promotion)
    '''

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap players

    '''
    Undo the last move made    
    '''
    def undoMove(self):
        if len(self.moveLog) != 0 : # Make sure there is a move to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #switch turns back

    
    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() 

    '''
    All moves wihtout considering checks
    '''
    def getAllPossibleMoves(self):
        moves = []
        for row in range(len(self.board)): #number of rows
            for col in range(len(self.board[row])): #number of cols in given row
                turn = self.board[row][col][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    if piece == 'p':
                        self.getPawnMoves(row,col, moves)
        return moves
    '''
    get all pawn moves for the pawn located at row, col and add these moves to the list
    '''

    def getPawnMoves(self, row, col, moves):
        pass

    '''
    get all rook moves for the pawn located at row, col and add these moves to the list
    '''

    def getRookMoves(self, row, col, moves):
        pass

    # '''
    # get all bishop moves for the pawn located at row, col and add these moves to the list
    # '''

    # def getbishopMoves(self, row, col, moves):
    #     pass

    # '''
    # get all knight moves for the pawn located at row, col and add these moves to the list
    # '''

    # def getKnightMoves(self, row, col, moves):
    #     pass

    # '''
    # get all knight moves for the pawn located at row, col and add these moves to the list
    # '''

    # def getKnightMoves(self, row, col, moves):
    #     pass 


        '''
    get all knight moves for the pawn located at row, col and add these moves to the list
    '''

    def getKnightMoves(self, row, col, moves):
        pass









class Move():
    # maps keys to values
    # keys : value

    ranksToRows = {"1" : 7, "2": 6, "3": 5, "4," : 4, "5" : 3, "6" : 2, "7" : 1, "8" : 0}
    
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}

    colsToFiles = {v: k for k, v in filesToCols.items()}



    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startCol = startSquare[1]
        self.endRow = endSquare[0]
        self.endCol = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    '''
    overriding the equals method
    '''

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        # you can add to make this real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]

