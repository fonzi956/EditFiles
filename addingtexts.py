file = open("texts.txt", "r")
newtexts = ""

def comments(line):
    if ('#' in line):
        line = line.replace('#', '<font color=\\\"green\\\">#') + ' </font>'
    return line

def charReplace(line):
    line = line.replace("\n", "")
    line = line.replace("'", "\\'")
    line = line.replace("`", "\\`")
    line = line.replace('"', '\\"')
    #line = line.replace('&', '&amp;')
    line = line.replace('<', '&lt;')
    line = line.replace('>', '&gt;')
    # if ('#' in line):
    #     line = line.replace('#', '<font color=\\\"green\\\">#') + ' </font>'

    # if (line[0:2] == "/*" or line[0:2] == "*/" or line[0:2] == "//" or line[0] == "#"):
    #     if (line[0:2] == "/*"):
    #         newtexts += '\t\t+"<br> <font color=\\\"green\\\">'+ line[:-1] + '"\n'
    #     elif (line[0:2] == "*/"):
    #         newtexts += '\t\t+"<br> '+ line[:-1] + '</font>"\n'
    #     elif (line[0:2] == "//" or line[0] == "#"):
    #         newtexts += '\t\t+"<br> <font color=\\\"green\\\">'+ line[:-1] + '</font>"\n'
    return line

# newtexts += '\t\t["' + file.readline().replace("\n", "").replace('# ', '') + '",\n'
# newtexts += '\t\t"'+ file.readline().replace("\n", "").replace('#', '<font color=\\\"green\\\">#') + ' </font>' + '\"\n'

for line in file:
    nob = 0
    for ni in line:
        if(ni == ' '):
            nob += 1
        else:
            break
    nos = nob
    nob /= 2
    if (nob > 0):
        line = charReplace(line)
        line = comments(line)
        newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\"\n"
    else:
        line = charReplace(line)
        if('{]' in line):
            newtexts += '\t\t'+ line.replace('{]', ',""],\n')
        elif('[}' in line):
            newtexts += '\t\t'+ line.replace('[}', '["').replace('#', '') + '",\n'
            start = True
        else:
            line = comments(line)
            if(start == True):
                start = False
                newtexts += '\t\t"<br> '+ line + '\"\n'
            else:
                newtexts += '\t\t+"<br> '+ line + '\"\n'
# newtexts += '\t\t,""],\n'
file.close()
newfile = open("newtexts.txt", "w")
newfile.write(newtexts)
newfile.close 



