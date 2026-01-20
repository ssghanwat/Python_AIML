def main():
    Ans = 0
    try:
        print("inside try...")

        print("enter first number : ")
        no1 = int(input())

        print("enter second number : ")
        no2 = int(input())

        Ans = no1/no2

    except:
        print("inside except..")

    finally:
        print("inside finally...")

    print("Division is : ",Ans)


if __name__ == "__main__":
    main() 