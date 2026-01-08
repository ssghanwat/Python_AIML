#One Function can Call another fucntion

def fun():
    print("inside fun")

def gun():
    print("inside gun")

def main():
    fun()
    gun()
    
if __name__ == "__main__":
    main()