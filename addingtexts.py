file = open("texts.txt", "r")
newtexts = ""

def comments(line):
    if ('#' in line):
        line = line.replace('#', '<font color=\\\"green\\\">#') + ' </font>'
    return line

def countFrom(nm, lin):
    nob = 0
    for ni in lin[nm:]:
        if(ni == ' '):
            nob += 1
        else:
            return nob

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

for line in file:
    nob = 0
    for ni in line:
        if(ni == ' '):
            nob += 1
        elif('[}' or '[0}' or '[+}' or '[-}' in line):
            if(line.find(' ') == 2 and '    ' in line):
                nob = countFrom(2, line)
                break
            elif(line.find(' ') == 3 and '    ' in line):
                nob = countFrom(3, line)
                break
            else:
                break        
        else:
            break
    nos = nob
    nob /= 2
    if (nob > 0):
        line = charReplace(line)
        if('[}' in line):
            line = line.replace('[}', '["').replace('#', '') + '",'
            newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\n"
            start = True
        elif('[0}' in line):
            line = line.replace('[0}', '["').replace('#', '') + '"'
            newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\n"
        elif('[+}' in line):
            line = line.replace('[+}', '+"').replace('#', '') + '"'
            newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\n"
        elif('[-}' in line):
            line = line.replace('[-}', '+"').replace('#', '') + '",'
            newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\n"
            start = True
        else:
            line = comments(line)
            if(start == True):
                start = False
                newtexts += "\t\t\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\"\n"
            else:
                newtexts += "\t\t+\"<br> "+ "&nbsp; "*int(nob) + line[nos:] + "\"\n"
    else:
        line = charReplace(line)
        if('{]' in line):
            newtexts += '\t\t'+ line.replace('{]', ',""],\n')
        elif('[}' in line):
            newtexts += '\t\t'+ line.replace('[}', '["').replace('#', '') + '",\n'
            start = True
        elif('[0}' in line):
            newtexts += '\t\t'+ line.replace('[0}', '["').replace('#', '') + '"\n'
        elif('[+}' in line):
            newtexts += '\t\t'+ line.replace('[+}', '+"<br>').replace('#', '') + '"\n'
        elif('[-}' in line):
            newtexts += '\t\t'+ line.replace('[-}', '+"<br>').replace('#', '') + '",\n'
            start = True
        else:
            line = comments(line)
            if(start == True):
                start = False
                newtexts += '\t\t"<br> '+ line + '\"\n'
            else:
                newtexts += '\t\t+"<br> '+ line + '\"\n'
file.close()
newfile = open("newtexts.txt", "w")
newfile.write(newtexts)
newfile.close 



