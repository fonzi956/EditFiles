import os
newtexts = ""
for filename in os.listdir(os.getcwd()):
    if (filename == "allfilesinone.py" or filename == "oneallfiles.txt"):
        continue
    with open(filename, 'r') as f:
        text = f.read()
        newtexts += text + "\n"

with open("oneallfiles.txt", "w") as f:
    f.write(newtexts)