def Multiplication(Value1, Value2):
    ans = 0 
    ans = Value1 * Value2
    return ans

def main():
    No1 = 10   #local varaible
    No2 = 0
    Result = 0
    
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Result = Multiplication(No1, No2)
    print("Multiplication is : ", Result)

#starter
if __name__ == "__main__":
    main()