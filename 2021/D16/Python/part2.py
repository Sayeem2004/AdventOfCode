import math
pos,binary = 0,""

def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    hexadecimal = fin.read().split("\n")[0].strip()
    length = len(hexadecimal) * 4
    decimal = int(hexadecimal, 16)
    global binary
    binary = bin(decimal)[2:].zfill(length)
    fout.write(str(solve()))

def adv(inc):
    global pos
    pos += inc
    return binary[pos-inc:pos]

def solve():
    adv(3)
    id = int(adv(3), 2)
    if (id == 4):
        val = ""
        while (binary[pos] == "1"): val += adv(5)[1:]
        val += adv(5)[1:]
        return int(val, 2)
    else:
        vals = []
        ind = int(adv(1), 2)
        if (ind == 0):
            length = int(adv(15), 2)
            curr = pos
            while (pos-curr < length): vals.append(solve())
        else:
            length = int(adv(11), 2)
            for i in range(length): vals.append(solve())
        if (id == 0): return sum(vals)
        elif (id == 1): return math.prod(vals)
        elif (id == 2): return min(vals)
        elif (id == 3): return max(vals)
        elif (id == 5): return (1 if vals[0] > vals[1] else 0)
        elif (id == 6): return (1 if vals[0] < vals[1] else 0)
        else: return (1 if vals[0] == vals[1] else 0)

main()
