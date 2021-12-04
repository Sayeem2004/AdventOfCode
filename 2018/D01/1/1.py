fin = open("1.in","r");
fout = open("1.out","w");

def main():
    nums = [num.strip() for num in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(nums)));

def solve(nums):
    ans = 0;
    for num in nums:
        if (num[0] == "+"): ans += int(num[1:]);
        else: ans -= int(num[1:]);
        return ans;

main();
