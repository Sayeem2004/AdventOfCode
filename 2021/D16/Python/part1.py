pos = 0
binary = ""


def main():
    fin = open("../input.in", "r")
    fout = open("../part1.out", "w")
    hexadecimal = fin.read().split("\n")[0].strip()
    length = len(hexadecimal) * 4
    decimal = int(hexadecimal, 16)
    global binary
    binary = bin(decimal)[2:].zfill(length)
    fout.write(str(solve()))


def solve():
    global pos
    sm = 0
    ver = int(binary[pos:pos+3], 2)
    pos += 3
    id = int(binary[pos:pos+3], 2)
    pos += 3
    if (id == 4):
        while (binary[pos] == "1"):
            pos += 5
        pos += 5
    else:
        ind = int(binary[pos], 2)
        pos += 1
        if (ind == 0):
            length = int(binary[pos:pos+15], 2)
            pos += 15
            curr = pos
            while (pos-curr < length):
                sm += solve()
        else:
            length = int(binary[pos:pos+11], 2)
            pos += 11
            for i in range(length):
                sm += solve()
    return ver+sm


main()
