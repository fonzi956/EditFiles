file = open("texts.txt", "r")
for line in file:
    nob = 0
    for ni in line:
        if(ni == ' '):
            nob += 1
        else:
            nob /= 4
            print("tab"*int(nob))
            break

file.close()
