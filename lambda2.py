#Functional Approach
# def checkEven(No):
    # return (No % 2 == 0)

checkEven = lambda No : No % 2 == 0

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