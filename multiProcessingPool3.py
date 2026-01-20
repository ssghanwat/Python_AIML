import time
import os

def sumCube(No):
    print("Process is running with :", os.getpid())
    sum = 0
    
    for i in range(1, No+1,1):
        sum = sum + (i ** 3)
    
    return sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000, 5000000,6000000,7000000,8000000,9000000,10000000]
    Result = []

    start_time = time.time()

    for i  in range(len(Data)):
        ret = sumCube(Data[i])
        Result.append(ret)

    end_time = time.time()

    print(Result)
    print("Totla execution time :", end_time - start_time)

if __name__ == "__main__":
    main() 


#Totla execution time : 6.322621822357178
