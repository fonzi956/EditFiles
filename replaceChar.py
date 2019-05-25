file = open("texts.txt", "r")
newtexts = ""

for line in file:
    if ('#' in line):
        line = line.replace("#", "<font color=\"green\">")
        #print("<font color=\"green\">" + line[:-1] + "</font>")
        newtexts += line[:-1] + "</font> \n"
    else:
        #print(line[:-1])
        newtexts += line[:-1] + "\n"
#print(newtexts)

file.close()
newfile = open("newtexts.txt", "w")
newfile.write(newtexts)
newfile.close 