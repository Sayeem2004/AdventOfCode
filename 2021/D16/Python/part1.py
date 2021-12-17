pos, binary = 0, ""

def main():
    fin, fout = open("../input.in", "r"), open("../part1.out", "w")
    hexadecimal = fin.read().split("\n")[0].strip()
    length = len(hexadecimal) * 4
    global binary
    binary = bin(int(hexadecimal, 16))[2:].zfill(length)
    fout.write(str(solve()))

def adv(inc):
    global pos
    pos += inc
    return binary[pos-inc:pos]

def solve():
    sm, id = int(adv(3), 2), int(adv(3), 2)
    if (id == 4):
        while (binary[pos] == "1"): adv(5)
        adv(5)
    else:
        ind = int(adv(1), 2)
        if (ind == 0):
            length, curr = int(adv(15), 2), pos
            while (pos-curr < length): sm += solve()
        else:
            length = int(adv(11), 2)
            for i in range(length): sm += solve()
    return sm

main()
