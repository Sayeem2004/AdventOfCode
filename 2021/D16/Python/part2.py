import math
pos = 0
binary = ""


def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    hexadecimal = fin.read().split("\n")[0].strip()
    length = len(hexadecimal) * 4
    decimal = int(hexadecimal, 16)
    global binary
    binary = bin(decimal)[2:].zfill(length)
    fout.write(str(solve()))


def solve():
    global pos
    global binary
    pos += 3
    id = int(binary[pos:pos+3], 2)
    pos += 3
    if (id == 4):
        val = ""
        while (binary[pos] == "1"):
            val += binary[pos+1:pos+5]
            pos += 5
        val += binary[pos+1:pos+5]
        pos += 5
        return int(val, 2)
    else:
        vals = []
        ind = int(binary[pos], 2)
        pos += 1
        if (ind == 0):
            length = int(binary[pos:pos+15], 2)
            pos += 15
            curr = pos
            while (pos-curr < length):
                vals.append(solve())
        else:
            length = int(binary[pos:pos+11], 2)
            pos += 11
            for i in range(length):
                vals.append(solve())
        if (id == 0):
            return sum(vals)
        elif (id == 1):
            return math.prod(vals)
        elif (id == 2):
            return min(vals)
        elif (id == 3):
            return max(vals)
        elif (id == 5):
            return (1 if vals[0] > vals[1] else 0)
        elif (id == 6):
            return (1 if vals[0] < vals[1] else 0)
        else:
            return (1 if vals[0] == vals[1] else 0)


main()
