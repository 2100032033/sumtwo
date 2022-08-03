import re
txt = "Use of python in machine learning"
x=re.search("^Use.*Learning$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")
