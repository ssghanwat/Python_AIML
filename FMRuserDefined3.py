checkEven = lambda No: (No % 2 == 0)
Increment =  lambda No : No + 1
Add = lambda a, b : a + b

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
    
        if Ret == True:
            Result.append(no)            

    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result

def reduceX(Task, Elements):
    Sum = 0

    # [11, 21, 23, 31]
    for no in Elements:
        Sum = Add(Sum, no)
    
    return Sum

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is :" , Data)

    FData = list(filterX(checkEven, Data))
    print("data after filter is :", FData)

    MData= list(mapX(Increment, FData))
    print("Data after map is :", MData)

    RData = reduceX(Add, MData)
    print("data after reduce is : ", RData)

if __name__=="__main__":
    main()