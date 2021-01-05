fin = open("1.in","r");
fout = open("1.out","w");

def main():
    lines = [line.strip()[:-1] for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" (contains ") for line in lines];
    names = [line[0].split(" ") for line in lines];
    contains = [line[1].split(", ") for line in lines];
    fout.write(str(solve(names,contains)));

def solve(names,contains):
    allergens = set();
    final = set();
    for con in contains:
        for c in con:
            allergens.add(c);
    for allergen in allergens:
        st = find(allergen,names,contains);
        for s in st:
            final.add(s);
    count = 0;
    for name in names:
        for n in name:
            if (not n in final):
                count += 1;
    return count;

def find(allergen,names,contains):
    ret = set();
    count = 0;
    for i in range(len(contains)):
        if (allergen in contains[i]):
            if (count == 0):
                for name in names[i]:
                    ret.add(name);
            else:
                s = set();
                for name in names[i]:
                    s.add(name);
                ret = ret.intersection(s);
            count+=1;
    return ret;

main();
