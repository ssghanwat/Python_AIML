
def EmployeeInfo(Name, Age, Salary, City = "Mumbai"):
    print("Name :", Name)
    print("Age :", Age)
    print("salary :", Salary)
    print("City", City)
    
def main():
    # EmployeeInfo()
    EmployeeInfo("Rahul", 26, 2000.50 , "Pune")

if __name__ == "__main__":
    main()