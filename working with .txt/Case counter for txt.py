def ccount():
    f = open('words.txt')
    low= 0
    up = 0
    data=f.read()
    for i in data:
        if i.isupper() and i.isalpha():
            up += 1
        elif i.islower() and i.isalpha():
            low += 1
    print('uppercase: ',up,"lowercase: ", low)
    f.close()            
if __name__ == "__main__":
    ccount()
