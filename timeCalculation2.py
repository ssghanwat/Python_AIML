import time

def Factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    return fact

def main():
    value = int(input("Enter number :"))

    start_time = time.time()

    result = Factorial(value)

    end_time = time.time()

    print("Factorial is :",result)

    print("total execution time is :", end_time - start_time)

if __name__ == "__main__":
    main() 