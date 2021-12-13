def main():
    fin = open("../input.in", "r")
    fout = open("../part1.out", "w")
    lines = [line.strip() for line in fin.read().split("\n\n")]
    nums = [[int(y) for y in x.split(",")] for x in lines[0].split("\n")]
    folds = [[int(y) if (q == 1) else y for q, y in enumerate(x.split("="))] for x in lines[1].split("\n")]
    fout.write(str(solve(nums, folds)))


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
        break
    lt = set()
    for num in nums:
        lt.add(",".join([str(x) for x in num]))
    return len(lt)


main()
