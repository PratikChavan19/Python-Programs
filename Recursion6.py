
def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)
        print(No)

def main():
    iNo = int(input("Enter Number : "))

    Display(iNo)

if __name__ == "__main__":
    main()