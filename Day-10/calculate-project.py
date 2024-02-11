#calculator
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1 ,n2):
    return n1/n2

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 =int(input("What's the first number?: "))
num2 =int(input("What's the first number?: "))
for symbol in operations:
    print (symbol)

operations_symbol=input("pick an operation from the above: ")

calculation_function= operations[operations_symbol]
answer = calculation_function(num1 , num2 )
print(f"{num1} {operations_symbol} {num2} = {answer}" )