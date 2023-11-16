def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1//num2

print("---------SIMPLE CALCULATOR-----------------")
print("Enter your choice-\n"\
      "1.ADD\n"\
      "2.SUBTRACT\n"\
      "3.MULTIPLY\n"\
      "4.DIVISON\n")
while True:
    choice=int(input("Select choice 1,2,3,4:"))
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    if choice==1:
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice==2:
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice==3:
        print(num1,"*",num2,"=",mul(num1,num2))
    elif choice==4:
        print(num1,"/",num2,"=",div(num1,num2))
    else:
        print("invalid input")
    

