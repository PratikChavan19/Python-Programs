# 4
# 4 * 3 * 2 * 1 -> 24

def Add(No):
    if(No <= 1):
        return 1
    else:
        return (No * Add(No - 1))

def main():
    iNo = int(input("Enter Number : "))

    Ret = Add(iNo)
    print("Result is : ", Ret)

if __name__ == "__main__":
    main()