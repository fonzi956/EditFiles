file = open("texts.txt", "r")
newtexts = ""
for line in file:
    nob = 0
    for ni in line:
        if(ni == ' '):
            nob += 1
        else:
            nos = nob
            nob /= 4
            if (nob > 0):
                line = line.replace("'", "\\'")
                line = line.replace("`", "\\`")
                line = line.replace('"', '\\"')
                newtexts += "+\"<br> "+ "&nbsp; "*int(nob) + line[nos:-1] + "\"\n"
                #print("+\"<br> "+ "&nbsp; "*int(nob) + line[:-2] + "\"")
            else:
                line = line.replace("'", "\\'")
                line = line.replace("`", "\\`")
                line = line.replace('"', '\\"')
                newtexts += '+"<br> '+ line[:-1] + '"\n'
                #print('+"<br> '+ line[:-2] + '"')
            break
#print(newtexts)
file.close()
newfile = open("newtexts.txt", "w")
newfile.write(newtexts)
newfile.close 