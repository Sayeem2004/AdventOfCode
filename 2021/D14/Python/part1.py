def main():
    fin = open("../input.in", "r")
    fout = open("../part1.out", "w")
    lines = [line.strip() for line in fin.read().split("\n\n")]
    lt = list(lines[0])
    dict = {}
    for line in lines[1].split("\n"):
        temp = line.split(" -> ")
        dict[temp[0]] = temp[1]
    fout.write(str(solve(lt, dict)))


def solve(lt, dict):
    for _ in range(10):
        cpy = [lt[0]]
        for i in range(1, len(lt)):
            temp = [lt[i-1], lt[i]]
            val = "".join(temp)
            if (val in dict):
                cpy.append(dict[val])
            cpy.append(lt[i])
        lt = cpy
    freq = {}
    for ch in lt:
        if (ch in freq):
            freq[ch] += 1
        else:
            freq[ch] = 1
    mx, mn = 0, 1000000
    for val in freq.keys():
        mx = max(mx, freq[val])
        mn = min(mn, freq[val])
    return mx-mn


main()
