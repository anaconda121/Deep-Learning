import sys

# print(sys.argv)

summ = 0
for i in range(1, len(sys.argv)):
    summ += int(sys.argv[i])
     
print("Sum:", summ)

