file1 = input("copy: ")
file2 = input("Paste: ")
f1 = open(file1, "r")
f2 = open(file2, "w")

line=f1.readline()
while line != "":
    f2.write(line)
    line = f1.readline() #opens next line important! 
f1.close()
f2.close()
