file = open("texts.txt", "r")
newtexts = ""

def charReplace(line):
    line = line.replace("'", "\\'")
    line = line.replace("`", "\\`")
    line = line.replace('"', '\\"')
    #line = line.replace('&', '&amp;')
    line = line.replace('<', '&lt;')
    line = line.replace('>', '&gt;')
    return line
newtexts += '\t\t["",\n'
for line in file:
    nob = 0
    for ni in line:
        if(ni == ' '):
            nob += 1
        else:
            nos = nob
            nob /= 2
            if (nob > 0):
                line = charReplace(line)
                newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:-1] + "\"\n"
            else:
                line = charReplace(line)
                if (line[0:2] == "/*" or line[0:2] == "*/" or line[0:2] == "//"):
                    if (line[0:2] == "/*"):
                        newtexts += '\t\t+"<br> <font color=\\\"green\\\">'+ line[:-1] + '"\n'
                    elif (line[0:2] == "*/"):
                        newtexts += '\t\t+"<br> '+ line[:-1] + '</font>"\n'
                    elif (line[0:2] == "//"):
                        newtexts += '\t\t+"<br> <font color=\\\"green\\\">'+ line[:-1] + '</font>"\n'
                else:
                    line = charReplace(line)
                    newtexts += '\t\t+"<br> '+ line[:-1] + '"\n'
            break
newtexts += '\t\t,""],\n'
file.close()
newfile = open("newtexts.txt", "w")
newfile.write(newtexts)
newfile.close 



