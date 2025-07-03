def calc(interval):
  firerate = 60000/interval 
  print("firerate is: ", firerate, "RPM")
  
while True:
 x = float(input("enter interval: "))
 calc(x)
 
 print("TTK is")
 for i in range(5):
  print(i+1,"bullets", x*i, "ms")
