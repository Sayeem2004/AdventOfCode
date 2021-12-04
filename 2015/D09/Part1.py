from itertools import permutations
fin = open("Input.in","r");
fout = open("Part1.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    places = set();
    dist = dict();
    for line in lines:
        a = line.split(" ");
        places.add(a[0]);
        places.add(a[2]);
        dist[a[0]+a[2]] = int(a[4]);
        dist[a[2]+a[0]] = int(a[4]);
    fout.write(str(solve(places,dist)));

def solve(places,dist):
    mn = 100000000;
    for perm in permutations(places):
        count = 0;
        for i in range(len(perm)-1):
            count += dist[perm[i]+perm[i+1]];
        mn = min(mn,count);
    return mn;

main();
