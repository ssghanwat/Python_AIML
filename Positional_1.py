def Display(A,B,C,D):
    print(A,B,C,D)
    
def main():
    # Display(10,20)           ----> Not Allowed less parameters
    # Display(10,20,30,40,50)  ----> Not Allowed more parameters
    Display(10,20,30,40)       #---> Allowed because of same number of parameters

if __name__ == "__main__":
    main()