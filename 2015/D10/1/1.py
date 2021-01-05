fin = open("1.in","r");
fout = open("1.out","w");

def main():
    num = fin.read().split("\n")[0].strip();
    fout.write(str(solve(num)));

def solve(num):
    for i in range(40):
        num = next(num);
    return len(num);

def next(num):
    ret = "";
    count = 1;
    if (len(num) == 1): return "1"+num;
    for i,x in enumerate(num):
        if (i == 0): continue;
        if (i == len(num)-1):
            if (num[i] != num[i-1]):
                ret += str(count)+num[i-1];
                ret += "1" + num[i]
            else: ret += str(count+1)+num[i];
            break;
        if (num[i] == num[i-1]): count += 1;
        else:
            ret += str(count)+num[i-1];
            count = 1;
    return ret;

main();
