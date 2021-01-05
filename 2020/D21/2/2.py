fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip()[:-1] for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" (contains ") for line in lines];
    names = [line[0].split(" ") for line in lines];
    contains = [line[1].split(", ") for line in lines];
    fout.write(str(solve(names,contains)));

def solve(names,contains):
    allergens = set();
    final = []; dict = {};
    for con in contains:
        for c in con:
            allergens.add(c);
    i = 0;
    for allergen in allergens:
        st = find(allergen,names,contains);
        dict[allergen] = i;
        final.append(list(st));
        i+=1;
    count = 0;
    for line in final:
        if (len(line) == 1): count+=1;
    while (count < len(final)):
        for fn in final:
            if (len(fn) == 1):
                name = fn[0];
                for f in final:
                    a = len(f)
                    if (name in f and a != 1):
                        f.remove(name);
                        if (len(f) == 1 and a != 1): count+=1;
    sorted = [];
    for d in dict: sorted.append(d);
    sorted.sort();
    ret = [];
    for s in sorted: ret.append(final[dict[s]][0])
    return ",".join(ret);

def find(allergen,names,contains):
    ret = set();
    count = 0;
    for i in range(len(contains)):
        if (allergen in contains[i]):
            if (count == 0):
                for name in names[i]: ret.add(name);
            else:
                s = set();
                for name in names[i]: s.add(name);
                ret = ret.intersection(s);
            count+=1;
    return ret;

main();
