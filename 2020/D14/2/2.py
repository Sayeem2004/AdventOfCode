fin = open("2.in","r");
fout = open("2.out","w");

def main():
    lines = [line.strip() for line in fin.read().split("\n")[0:-1]];
    lines = [line.split(" = ") for line in lines];
    fout.write(str(solve(lines)));

def solve(lines):
    memory = {};
    mask = list(lines[0][1]);
    for line in lines:
        if (line[0] == "mask"): mask = list(line[1]);
        else:
            value = int(line[1]);
            initial = int(line[0][4:-1]);
            final = [];
            location = (36-(len(bin(initial))-2))*"0" + bin(initial)[2:];
            for i in range(len(mask)):
                if mask[i] == "0": final.append(location[i]);
                else: final.append(mask[i]);
            subsets = ["".join(final)]
            for i in range(len(final)):
                temporary = [];
                if final[i] == "X":
                    for sub in subsets:
                        temporary.append(sub[:i]+"1"+sub[i+1:]);
                        temporary.append(sub[:i]+"0"+sub[i+1:]);
                    subsets = temporary;
            subsets = [int("0b"+sub,2) for sub in subsets];
            for sub in subsets: memory[sub] = value;
    sum = 0;
    for mem in memory: sum += memory[mem];
    return sum;
    
main();
