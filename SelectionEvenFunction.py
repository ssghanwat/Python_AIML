def checkEven(No):
    if (No % 2) == 0:
        print("No is Even")
    else:
        print("No is Odd")


def main():
    # No = int(input("Enter number to check :"))
    checkEven(21)     #positional argument
    checkEven(No = 22)#keyworg argument


if __name__=="__main__":
    main()