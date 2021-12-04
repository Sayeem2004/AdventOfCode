fin = open("1.in","r");
fout = open("1.out","w");

def main():
    nums = [int(num.strip()) for num in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(nums)));

def solve(nums):
    n = len(nums);
    for i in range(n):
        for q in range(i+1,n):
            if (nums[i]+nums[q] == 2020):
                return nums[i]*nums[q];
                break;

main();
