#Procedural 

def checkEven(No):
    if (No % 2) == 0:
        print("No is Even")
    else:
        print("No is Odd")

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    checkEven(Value)

if __name__=="__main__":
    main()