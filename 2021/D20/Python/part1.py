def main():
    fin, fout = open("../input.in", "r"), open("../part1.out", "w")
    lines = [line.strip() for line in fin.read().split("\n\n")]
    key = list(lines[0])
    img = [list(x) for x in lines[1].split("\n")]
    fout.write(str(solve(img, key)))

def enhance(img, key):
    ret = [["." for x in range(len(img[0])+2)] for y in range(len(img)+2)]
    for y in range(0, len(ret)):
        for x in range(0, len(ret[0])):
            val = ""
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny = y+dy
                    if (ny < 1 or ny >= len(ret)-1):
                        val += "0"
                        continue
                    nx = x+dx
                    if (nx < 1 or nx >= len(ret[0])-1):
                        val += "0"
                        continue
                    val += "1" if img[ny-1][nx-1] == "#" else "0"
            ret[y][x] = key[int(val, 2)]
    return ret

def solve(img, key):
    for i in range(2):
        img = enhance(img, key)
    cnt = 0
    for i in range(len(img)):
        for q in range(len(img[0])):
            cnt += 1 if img[i][q] == "#" else 0
    return cnt

main()
