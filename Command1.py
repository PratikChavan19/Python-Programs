from sys import *

def main() :
    print("Total number of arguments are : ", len(argv))

    print("Name of application : ", argv[0])

    print("First argument of  :", argv[1])
    print("Second argument of  :", argv[2])
    print("Third argument of  :", argv[3])

if __name__ == "__main__" :
    main()

#                       0             1         2       3
# python Command1.py 12     Hello   21