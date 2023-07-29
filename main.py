import re

in_name = "input.txt"

with open("find.txt","r") as f, open("repl.txt","r") as r, open(in_name,"r") as i, open("output.txt","w") as o: 
    find = f.readlines()
    repl = r.readlines()
    inpt = i.read()
    if len(find) != len(repl):
        raise RuntimeError("Find and Replace files different lengths")
    for x in range(len(find)):
        # strip off the \n
        find[x] = find[x][:-1]
        repl[x] = repl[x][:-1]
        inpt = re.sub(find[x],repl[x],inpt)
    o.write(inpt)