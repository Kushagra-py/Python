#store integers and prints them
import pickle

file = open('data.dat', 'wb')
while True:
    x=int(input("integer: "))
    pickle.dump(x,file)
    a=input("continue: y/n")
    if a== "n":
        break
file.close()
file = open('data.dat', 'rb')
try:
    while True:
        y = pickle.load(file)
        print(y)
except EOFError:
    pass 
file.close()   