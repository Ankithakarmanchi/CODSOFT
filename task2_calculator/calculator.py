# Simple Calculator
def choose_operation():
    print("\n Choose any operation among this:")
    print("\n + , - , * , / , % , **")
    op=input("Enter operation(+,-,*,/,%,**):").strip()
    return op
def calculator(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        if num2==0:
            return "Error: Divisor can't be zero , please choose another input num2"
        return num1/num2
    elif op=='%':
        if num2==0:
            return "Error: Divisor can't be zero, please choose another input num2"
        return num1/num2
    elif op=='**':
        return num1**num2
    else:
        return "error: Unknown operation , please choose valid operation"
def main():
    print("--- task2:Simple Calculator---")
    while True:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        op=choose_operation()
        result=calculator(num1,num2,op)
        print(f"\nResult:{result}")
        again=input("\n Do another calculation,if yes enter y else n?(y/n):").strip().lower()
        if again!='y':
            print("Thankyou...! \n Keep doing, All the best")
            break
if __name__ == "__main__":
    main()