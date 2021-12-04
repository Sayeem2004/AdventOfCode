fin = open("2.in","r");
fout = open("2.out","w");

def main():
    nums = [num.strip() for num in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(nums)));

def solve(nums):
    ans = 0; br = True;
    prev = set(); prev.add(ans);
    while (br):
        for num in nums:
            if (num[0] == "+"): ans += int(num[1:]);
            else: ans -= int(num[1:]);
            if (ans in prev):
                return ans;
                br = False; break;
            prev.add(ans);

main();
