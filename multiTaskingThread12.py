import multiprocessing
import time
import os

def sumEven(No):
    print("PID of sumEven : ", os.get_pid()) # 51
    print("PPID of sumEven : ", os.get_ppid()) # 21
    iSum = 0
    for i in range(2, No+1,2):
        iSum = iSum + i
    print("Even sum is :", iSum)


def sumOdd(No):
    print("PID of sumOdd :", os.get_pid()) # 101
    print("PPID of sumOdd : ", os.get_ppid()) # 21

    iSum = 0
    for i in range(1, No+1,2):
        iSum = iSum + i
    print("Odd sum is :", iSum) 

def main():
    print("PID of main :", os.get_pid()) # 21
    print("PPID of main : ", os.get_ppid()) #terminal - 11

    start_time = time.time()

    p1 = multiprocessing.process(target = sumEven, args = (1000,))
    p2 = multiprocessing.process(target = sumOdd, args = (1000,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()

    print("time required :", end_time - start_time)

if __name__ == "__main__":
    main() 