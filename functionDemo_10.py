#One Function can Call another function

def fun():
    print("inside fun")

def gun():
    print("inside gun")
    fun()

def main():
    # fun()
    gun()
    
if __name__ == "__main__":
    main()