print("Addition - 1")
print("Subtraction - 2")
print("Multiplication - 3")
print("Division - 4")
print("Remainder - 5")
z=int(input("Enter the mode of Operation : "))
a=int(input("Enter the First value: "))
b=int(input("Enter the Second Value: "))
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
if(z==1):
  print("The Result Value is : ",c)
elif(z==2):
  print("The Result Value is : ",d)
elif(z==3):
  print("The Result Value is : ",e)
elif(z==4):
  print("The Result Value is : ",f)
elif(z==5):
  print("The Result Value is : ",g)
else:
  print("Enter the proper operator")
  
