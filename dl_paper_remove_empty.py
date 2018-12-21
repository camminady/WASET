import os, glob

os.chdir("publications")
for file in glob.glob("*.pdf"):
    s = os.path.getsize(file)
    print(s)
    if int(s) == 14 : 
        # delete empty file
        os.remove(file)
