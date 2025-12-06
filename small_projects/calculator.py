# Global list to store calculation history
history_list = []

#Functions for each operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "float division by zero"
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return "float division by zero"
    return a % b

def history():
    """Display the calculation history"""
    if not history_list:
        print("No past calculations to show")
    else:
        for calculation in history_list:
            print(calculation)

#choise of operator

def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice == '?':
        history()
        return 0
    elif choice in ('+', '-', '*', '/', '^', '%'):
        # Get first number
        num1_input = input("Enter first number: ")
        print(num1_input)
        if num1_input == '':
            return 0
        if num1_input == '$':
            return 0
        if num1_input.endswith('$'):
            return 0
        if num1_input == '#':
            return -1
        if num1_input.endswith('#'):
            return -1
        
        try:
            num1 = float(num1_input)
        except ValueError:
            print("Not a valid number,please enter again")
            return 0
        
        # Get second number
        num2_input = input("Enter second number: ")
        print(num2_input)
        if num2_input == '':
            return 0
        if num2_input == '$':
            return 0
        if num2_input.endswith('$'):
            return 0
        if num2_input == '#':
            return -1
        if num2_input.endswith('#'):
            return -1
        
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Not a valid number,please enter again")
            return 0
        
        # Perform calculation
        result = None
        try:
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)
            elif choice == '^':
                result = power(num1, num2)
            elif choice == '%':
                result = remainder(num1, num2)
            
            # Display result and save to history
            if isinstance(result, str):  # Error message for division by zero
                print(result)
                print(f"{num1} {choice} {num2} = None")
                # Save failed calculation to history
                history_list.append(f"{num1} {choice} {num2} = None")
            else:
                # Always display as floats with .0 format
                print(f"{num1} {choice} {num2} = {result}")
                # Save successful calculation to history
                history_list.append(f"{num1} {choice} {num2} = {result}")
                
        except Exception as e:
            print("Something Went Wrong")
            
        return 0
    else:
        print("Unrecognized operation")
        return 0

#End the select_op(choice) function here

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    print("*"*40)
    print("/n Learn with Sithum")
    exit()
    
