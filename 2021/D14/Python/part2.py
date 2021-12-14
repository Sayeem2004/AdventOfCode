def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    lines = [line.strip() for line in fin.read().split("\n\n")]
    lt = list(lines[0])
    freq = {}
    for i in range(1, len(lt)):
        tmp = lt[i-1]+lt[i]
        if (tmp in freq):
            freq[tmp] += 1
        else:
            freq[tmp] = 1
    dict = {}
    for line in lines[1].split("\n"):
        temp = line.split(" -> ")
        dict[temp[0]] = [temp[0][0]+temp[1], temp[1]+temp[0][1]]
    fout.write(str(solve("".join(lt), freq, dict)))


def solve(initial, freq, dict):
    for _ in range(40):
        cpy = {}
        for f in freq.keys():
            temp = dict[f]
            if (temp[0] in cpy):
                cpy[temp[0]] += freq[f]
            else:
                cpy[temp[0]] = freq[f]
            if (temp[1] in cpy):
                cpy[temp[1]] += freq[f]
            else:
                cpy[temp[1]] = freq[f]
        freq = cpy
    ret = {}
    for f in freq.keys():
        if (f[0] in ret):
            ret[f[0]] += freq[f]
        else:
            ret[f[0]] = freq[f]
        if (f[1] in ret):
            ret[f[1]] += freq[f]
        else:
            ret[f[1]] = freq[f]
    ret[initial[0]] += 1
    ret[initial[-1]] += 1
    mx, mn = 0, 1000000000000000
    for r in ret.keys():
        ret[r] /= 2
        mx = max(mx, ret[r])
        mn = min(mn, ret[r])
    return mx-mn


main()
