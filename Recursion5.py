
def Display(No):
    if(No > 0):
        print(No)
        No = No - 1
        Display(No)

def main():
    iNo = int(input("Enter Number : "))

    Display(iNo)

if __name__ == "__main__":
    main()