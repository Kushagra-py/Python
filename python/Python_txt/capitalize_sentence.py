import os
def capitalize_sentence():
    f1=open("Uncapitalized.txt")
    f2=open("capatilized.txt","w")
    while True: 
        line = f1.readline()
        if not line:
            break #EOF
        line = line.rstrip() #strips newline chr
        linelength = len(line)
        string=""
        string += line[0].upper() #first letter
        i=1
        while i<linelength:
            if line[i]==".": #after full stop
                string += line[i]
                i+=1
                if i>=linelength:
                    break #EOF
                string += line[i].upper()
            else:
                string += line[i]            
            i += 1
        f2.write(string)  
    f1.close() 
    f2.close()

capitalize_sentence()
