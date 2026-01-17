from functools import reduce

def checkEven(No):
    return No % 2 == 0

def Increment(No):
    return No+1

def Add(a, b):
    return a + b

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is :" , Data)

    FData = list(filter(checkEven, Data))
    print("data after filter is :", FData)

    MData= list(map(Increment, FData))
    print("Data after map is :", MData)

    RData = reduce(Add, MData)
    print("data after reduce is : ", RData)

if __name__=="__main__":
    main()