def main():
    Ans = 0
    try:
        print("inside try...")

        print("enter first number : ")
        no1 = int(input())

        print("enter second number : ")
        no2 = int(input())

        Ans = no1/no2

    except ZeroDivisionError as zobj:
        print("inside except : ", zobj)

    except ValueError as vobj:
        print("inside except : ", vobj)

    except Exception as eobj:
        print("inside except : ", eobj)

    finally:
        print("inside finally...")

    print("Division is : ",Ans)


if __name__ == "__main__":
    main() 