class Dictionary(object):
    WORDS = set(['red', 'blue', 'green', 'cyan'])

    @staticmethod
    def is_valid_word(word):
        return word in Dictionary.WORDS


def __solve_boggle(board, i, j, word, history):
    if len(history) == len(board) * len(board[0]):
        print word
        return

    r_del = [-1, -1, -1,  0, 0,  1, 1, 1]
    c_del = [-1,  0,  1, -1, 1, -1, 0, 1]

    word += board[i][j]
    if Dictionary.is_valid_word(word):
        print word

    for x in xrange(len(r_del)):
        r, c = i+r_del[x], j+c_del[x]
        if r >= 0 and c >= 0 and r < len(board) and c < len(board[r]) and (r,c) not in history:
            history.add((i, j))
            __solve_boggle(board, r, c, word, history)
            history.remove((i, j))


def solve_boggle(board):
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            history = set([])
            word = ''
            __solve_boggle(board, i, j, word, history)

board = [['g', 'u', 'd'],
         ['l', 'r', 'e'],
         ['b', 'n', 'e']]
solve_boggle(board)