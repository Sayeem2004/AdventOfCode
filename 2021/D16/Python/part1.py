pos,binary = 0,""

def main():
    fin = open("../input.in", "r")
    fout = open("../part1.out", "w")
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
    sm = int(adv(3), 2)
    id = int(adv(3), 2)
    if (id == 4):
        while (binary[pos] == "1"): adv(5)
        adv(5)
    else:
        ind = int(adv(1), 2)
        if (ind == 0):
            length = int(adv(15), 2)
            curr = pos
            while (pos-curr < length): sm += solve()
        else:
            length = int(adv(11), 2)
            for i in range(length): sm += solve()
    return sm

main()
