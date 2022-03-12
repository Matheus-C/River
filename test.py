f = open("river.txt", "r")

f.readline()
a = f.readline().split()
print(a[1][1])