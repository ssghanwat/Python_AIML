import threading
import time

def sumEven(No):
    iSum = 0
    for i in range(2, No+1,2):
        iSum = iSum + i
    print("Even sum is :", iSum)    

def sumOdd(No):
    iSum = 0
    for i in range(1, No+1,2):
        iSum = iSum + i
    print("Odd sum is :", iSum) 

def main():
    start_time = time.time()
    sumEven(100000000)
    sumOdd(100000000)
    end_time = time.time()

    print("time required :", end_time - start_time)

if __name__ == "__main__":
    main() 