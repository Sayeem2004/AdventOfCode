from itertools import permutations
fin = open("Input.in","r");
fout = open("Part2.out","w");

def main():
    lines = [line.strip().split(" ") for line in fin.read().split("\n")[0:-1]];
    dict = {}; st = set();
    for line in lines:
        st.add(line[0]);
        st.add(line[-1][:-1]);
        if (line[2] == "gain"):
            dict[line[0]+line[-1][:-1]] = int(line[3]);
        else:
            dict[line[0]+line[-1][:-1]] = int(line[3])*-1;
    for s in st:
        dict["Mo"+s] = 0;
        dict[s+"Mo"] = 0;
    st.add("Mo")
    fout.write(str(solve(dict,st)));

def solve(dict,st):
    ans = -1000000000;
    for perm in permutations(st):
        ans = max(count(dict,perm),ans);
    return ans;

def count(dict,perm):
    ret = 0;
    n = len(perm)
    for i in range(n):
        ret += dict[perm[i%n]+perm[(i-1)%n]];
        ret += dict[perm[i%n]+perm[(i+1)%n]];
    return ret;

main();
