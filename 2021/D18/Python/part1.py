def main():
    fin, fout = open("../input.in", "r"), open("../part1.out", "w")
    lines = [eval(line.strip()) for line in fin.read().split("\n")[0:-1]]
    fout.write(str(solve(lines)))

def check(pair, depth):
    if (isinstance(pair, int)): return (pair >= 10)
    else: return (check(pair[0], depth+1) or check(pair[1], depth+1) or depth >= 4)

def add(pair, val, mode):
    if (isinstance(pair, int)):
        pair += val
        return pair
    else:
        if (mode == "r"): return [pair[0], add(pair[1], val, "r")]
        if (mode == "l"): return [add(pair[0], val, "l"), pair[1]]

def simplify(pair, depth):
    if (not isinstance(pair, int)):
        sl, sr = 0, 0
        while (check(pair[0], depth+1)):
            [pair[0], l1, r1] = simplify(pair[0], depth+1)
            pair[1] = add(pair[1], r1, "l")
            if (l1 != 0): return [pair, l1, 0]
        while (check(pair[1], depth+1)):
            [pair[1], l2, r2] = simplify(pair[1], depth+1)
            pair[0] = add(pair[0], l2, "r")
            if (r2 != 0): return [pair, 0, r2]
        if (depth >= 4): return [0, sl+pair[0], sr+pair[1]]
        else: return [pair, sl, sr]
    else:
        if (pair >= 10): return [[(pair-1)//2, (pair+1)//2], 0, 0]
        else: return [pair, 0, 0]

def solve(lines):
    curr = lines[0]
    for line in lines[1:]:
        curr = [curr, line]
        while (check(curr, 0)):
            [curr, l, r] = simplify([curr, line], 0)
    return curr
main()
