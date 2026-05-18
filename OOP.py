# Accept 2 numbers and perform addition and substraction from it

# Kay karayche ahe?         ->  Behaviours(Functions)
#       Addition and Substraction

# Te karayla kay lagnar ahe?        -> Characteristics(Data)
#           2 Numbers

# Class = Characteristics + Behaviours
# Class = Data + Functions


class Arithmatic :
    def __init__(self, A, B) :
        self.No1 = A
        self.No2 = B

    def Add(self) :
        return self.No1 + self.No2

    def Sub(self) :
        return self.No1 - self.No2

def main() :
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    obj = Arithmatic(Value1, Value2)

    Ans = obj.Add()             #0X100.Add()    ->  Add(0X100)
    print("Addition is : ", Ans)

    Ans = obj.Sub()             #0X100.Sub()    ->  Sub(0X100)
    print("Substraction is : ", Ans)

if __name__ == "__main__" :
    main()