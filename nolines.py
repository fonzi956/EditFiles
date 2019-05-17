file = open("texts.txt", "r")
nolinestext = file.read().replace('\n',' ')  
file.close()
newfile = open("newtexts.txt", "w")
newfile.write(nolinestext)
newfile.close 