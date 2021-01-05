fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip().split(" ") for line in fin.read().split("\n")[0:-1]];
    fout.write(str(solve(lines)));

def solve(lines):
    ans = 0;
    for line in lines:
        ans += calc(line);
    return ans;

def calc(equation):
    sum,skipto = 0,0;
    if ("(" in equation[0]):
        next = find(equation,0);
        skipto = next[-1];
        next = next[:-1];
        sum = calc(next);
    else: sum = int(equation[0]);
    for i in range(1,len(equation)):
        if (i < skipto): continue;
        if (equation[i] == "*"):
                sum *= calc(equation[i+1:]); return sum;
        if (equation[i] == "+"):
            if (not "(" in equation[i+1]):
                sum += int(equation[i+1]); continue;
            else:
                next = find(equation,i+1);
                skipto = next[-1];
                next = next[:-1];
                sum += calc(next);
    return sum;

def find(equation,index):
    next = []
    count = equation[index].count("(");
    next.append(equation[index][1:]);
    q = index+1;
    while (count != 0):
        if ("(" in equation[q]):
            count+=equation[q].count("(");
            next.append(equation[q]);
        elif (")" in equation[q]):
            count-=equation[q].count(")");
            if (count == 0): next.append(equation[q][:-1]);
            else: next.append(equation[q]);
        else: next.append(equation[q]);
        q+=1;
    return next+[q];

main();
