import copy

def nqueen(N):
    solutions = []
    columns = [-1 for _ in xrange(N)]
    __nqueen(columns, 0, N, solutions)
    return solutions

def __nqueen(columns, n, N, solutions):
    if n == N:
        solutions.append(copy.deepcopy(columns))
    else:
        for i in xrange(N):
            if is_valid_position(n, i, columns):
                columns[n] = i
                __nqueen(columns, n+1, N, solutions)

def is_valid_position(row_position, column_position, columns):
    for i in xrange(row_position):
        if columns[i] == column_position:
            return False
        if abs(columns[i] - column_position) == (row_position - i):
            return False
    return True


def print_nqueen_solutions(N):
    for n, solution in enumerate(nqueen(N)):
        print 'Solution #{}'.format(n + 1)
        for i in xrange(N):
            for j in xrange(N):
                if j == solution[i]:
                    print 1,
                else:
                    print 0,
            print


print_nqueen_solutions(N=8)
