import sys

names = []
 
for line in sys.stdin:
    # rstrip strips leading and trailing whitespace
    if '' == line.rstrip():
        break
    names.append(line[:len(line)-1])
 
print(names)
