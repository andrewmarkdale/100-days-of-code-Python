"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
10

Project:
Calculator

"""

from art import logo

def add(n1, n2):
    """Returns n1 + n2"""
    return n1 + n2

def multiply(n1, n2):
    """Returns n1 * n2"""
    return n1 * n2

def divide(n1, n2):
    """Returns n1 / n2"""
    return n1 / n2

def subtract(n1, n2):
    """Returns n1 - n2"""
    return n1 - n2

calculator_fn_dict = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
}

def get_operator():
    operation = input("Enter an option from the operator list: ")
    if operation in calculator_fn_dict.keys():
        return operation
    else:
        print("Invalid operator entry. Please select from the list of available operators.\n")
        return get_operator()
    
def get_num(position):
    try:
        num = float(input(f"Enter the {position} input: "))
        return num
    except KeyboardInterrupt:
        print() # Making it prettier for the console.
        quit()
    except:
        print(f"Invalid entry for {position} number. Try again.\n")
        return get_num(position)
    
def calc_loop():
    
    print()
    num1 = get_num("first")
    operation = get_operator()
    num2 = get_num("second")
    

    answer = calculator_fn_dict[operation](num1, num2)
    print(f"The result of {num1} {operation} {num2} = {answer}")
    
    while True:
        cont = input(f"Do you want to continue calculating with {answer}? Y/N or type E to exit: ")
        if cont.lower() == 'e':
            print("Goodbye!")
            quit()
        elif cont.lower() == 'n':
            calc_loop()
        elif cont.lower() != 'y':
            print("Invalid entry!")
            continue
        
        operation = get_operator()
        cont_num = get_num("next")
        old_answer = answer
        answer = calculator_fn_dict[operation](old_answer, cont_num)
        
        print(f'The result of {old_answer} {operation} {cont_num} = {answer}')
        
        
    
    

if __name__ == '__main__':
    print(logo)
    print("Operators:")
    for operator in calculator_fn_dict:
        print(operator)
    calc_loop()