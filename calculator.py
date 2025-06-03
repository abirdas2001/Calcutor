from addition import *
from substraction import *
from multiplecation import *
from divition import *
def main():
    print("1 - Addition")
    print("2 - Substraction")
    print("3 - Multiplecation")
    print("4 - square")
    print("5 - Divition")
    while True:
        choice = input("Enter your choice between 1 to 5 : ")
        num1=int(input("enter the first no :"))
        num2=int(input("enter the second no :"))
        if choice == "1":
            add(num1,num2)
            break
        elif choice == "2":
            sub(num1,num2)
            break
        elif choice == "3":
            mul(num1,num2)
            break
        elif choice == "4":
            squre(num1,num2) 
            break
        elif choice == "5":
            div(num1,num2)
        else:
            print("Invalid entry, please enter a choice between 1 to 4")
            break
main()