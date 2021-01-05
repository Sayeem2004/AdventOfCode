fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n\n")];
    player1 = [int(line) for line in lines[0].split("\n")[1:]];
    player2 = [int(line) for line in lines[1].split("\n")[1:]];
    fout.write(str(solve(player1,player2)));

def solve(player1,player2):
    final = recursion(player1,player2);
    ans = 0;
    if (final[2] == 1):
        a = len(final[0]);
        for i,x in enumerate(final[0]):
            ans += x * (a-i);
    else:
        a = len(final[1]);
        for i,x in enumerate(final[1]):
            ans += x * (a-i);
    return ans;

def recursion(player1,player2):
    previous = []; c = False;
    while (len(player1) != 0 and len(player2) != 0):
        cards = ["".join([str(p) for p in player1]),"".join([str(p) for p in player2])];
        if (cards in previous):
            a = player1[0]; b = player2[0];
            player1.pop(0); player2.pop(0);
            player1.append(a); player1.append(b);
            c = True; break;
        previous.append(cards);
        a = player1[0]; b = player2[0];
        player1.pop(0); player2.pop(0);
        if (a <= len(player1) and b <= len(player2)):
            final = recursion(player1[:a],player2[:b]);
            if (final[2] == 1): player1.append(a); player1.append(b);
            else: player2.append(b); player2.append(a);
            continue;
        if (a > b): player1.append(a); player1.append(b);
        else: player2.append(b); player2.append(a);
    if (c): return [player1,player2,1];
    if (len(player1) != 0): return [player1,player2,1];
    else: return [player1,player2,2];

main();
