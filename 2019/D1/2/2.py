fin = open("2.in","r");
fout = open("2.out","w");

def main():
    nums = [int(num.strip()) for num in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(nums)));

def solve(nums):
    ans = 0;
    for num in nums:
        temp = num;
        while (temp >= 9):
            temp = temp//3;
            temp -= 2;
            ans += temp;
    return ans;

main();
