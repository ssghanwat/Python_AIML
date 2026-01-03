def Multiplication(Value1, Value2):
    ans = 0 #Local Variable
    ans = Value1 * Value2
    return ans


# No1 = 0, No2 = 0, Result = 0        -----Not allowed Single line variable creation
No1 = 10
No2 = 0
Result = 0
No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

Result = Multiplication(No1, No2)
print("Multiplication is : ", Result)

##################################################################################

No1 = int(input("Enter First Number : "))
No2 = int(input("Enter Second Number : "))

Result = Multiplication(No1, No2)
print("Multiplication is : ", Result)