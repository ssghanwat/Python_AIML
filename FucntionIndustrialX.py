#Procedural 

def checkEven(No):
    if (No % 2) == 0:
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter Number : ")
    Value = int(input())

    Ret = checkEven(Value)
    
    if Ret == True:
        print("number is even")
    else:
        print("number is odd")

if __name__=="__main__":
    main()