# 4
# 4 + 3 + 2 + 1 -> 10

def Add(No):
    Ans = 0
    while(No >= 0):
        Ans = Ans + No
        No = No - 1

    return Ans

def main():
    iNo = int(input("Enter Number : "))

    Ret = Add(iNo)
    print("Result is : ", Ret)

if __name__ == "__main__":
    main()