fin = open("../Input.in", "r");
fout = open("../Part1.out", "w");

def main():
    lines = [line.strip() for line in fin.read().split("\n\n")];
    lines = [[[int(x) for x in row.split()] for row in line.split("\n")] if i != 0 else [int(x) for x in line.split(",")] for i,line in enumerate(lines)];
    fout.write(str(solve(lines)));

def add(board, num):
    for i in range(5):
        for q in range(5):
            if (board[i][q] == num):
                board[i][q] = -1;
                break;
    return board;

def check(board):
    for i in range(5):
        good1,good2 = True,True;
        for q in range(5):
            if (board[i][q] != -1): good1 = False;
            if (board[q][i] != -1): good2 = False;
        if (good1 == True or good2 == True): return True;
    return False;

def sum(board):
    sum = 0;
    for i in range(5):
        for q in range(5):
            if (board[i][q] != -1): sum += board[i][q];
    return sum;

def solve(lines):
    for x in lines[0]:
        for board in lines[1:]:
            board = add(board, x);
            if (check(board)):
                return sum(board) * x;

main();
