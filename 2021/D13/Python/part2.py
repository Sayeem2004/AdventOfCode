def main():
    fin = open("../input.in", "r")
    fout = open("../part2.out", "w")
    lines = [line.strip() for line in fin.read().split("\n\n")]
    nums = [[int(y) for y in x.split(",")] for x in lines[0].split("\n")]
    folds = [[int(y) if (q == 1) else y for q, y in enumerate(x.split("="))] for x in lines[1].split("\n")]
    ret = solve(nums, folds)
    for i in range(len(ret[0])):
        for q in range(len(ret)):
            fout.write(ret[q][i])
            fout.write(" ")
        fout.write("\n")


def solve(nums, folds):
    for fold in folds:
        if (fold[0][-1] == "x"):
            for num in nums:
                if (num[0] > fold[1]):
                    num[0] = fold[1]-(num[0]-fold[1])
        else:
            for num in nums:
                if (num[1] > fold[1]):
                    num[1] = fold[1]-(num[1]-fold[1])
    lt = [[" " for i in range(6)] for q in range(40)]
    for num in nums:
        lt[num[0]][num[1]] = "#"
    return lt


main()
