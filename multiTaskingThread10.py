import threading

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
    sumEven(100000000)
    sumOdd(100000000)
    
if __name__ == "__main__":
    main() 