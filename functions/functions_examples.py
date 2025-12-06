# Example 1: Basic Function with No Parameters
# This is my first function – it just says hi like a friendly robot.
def greet_the_world():
    """Prints a warm greeting to everyone.
    
    No inputs needed – super simple!
    """
    print("Hello, amazing world! 🌍 Let's code something awesome today!")

# Example 2: Function with Parameters
def add_two_numbers(a, b):
    """Adds two numbers and returns the sum.
    
    Args:
        a (int or float): First number.
        b (int or float): Second number.
    
    Returns:
        int or float: The sum of a and b.
    """
    result = a + b
    print("Adding",(a)," and ", (b)," gives us ",(result),"! ➕")
    return result

# Example 3: Function with Default Parameters
# Personalizing greetings – because everyone deserves a custom hello!
def personalized_greeting(name, time_of_day="morning"):
    """Creates a greeting based on name and time.
    
    Args:
        name (str): The person's name.
        time_of_day (str, optional): Time like 'morning' or 'evening'. Defaults to 'morning'.
    
    Returns:
        str: A personalized greeting message.
    """
    greeting = f"Good {time_of_day}, {name}! Hope your day is filled with code and coffee! ☕"
    return greeting

# Example 4: Function Returning Multiple Values
# Calculating BMI – my way of staying healthy while learning functions.
def calculate_bmi(weight_kg, height_m):
    """Calculates BMI and gives a simple category.
    
    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.
    
    Returns:
        tuple: (bmi_value, category) where category is a string.
    """
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight – eat more veggies! 🥦"
    elif 18.5 <= bmi < 25:
        category = "Normal – you're doing great! 👍"
    elif 25 <= bmi < 30:
        category = "Overweight – maybe add some walks? 🚶"
    else:
        category = "Obese – consult a doc for tips! 🩺"
    return round(bmi, 2), category

# Small Project: Simple To-Do List Manager using Functions
# I built this mini-app to practice functions – add tasks and list them!
def add_task(tasks, task):
    """Adds a task to the list.
    
    Args:
        tasks (list): The current list of tasks.
        task (str): The new task to add.
    
    Returns:
        list: Updated tasks list.
    """
    tasks.append(task)
    print("Added: '",(task),"' – one step closer to productivity! ✅")
    return tasks

def list_tasks(tasks):
    """Prints all tasks in the list.
    
    Args:
        tasks (list): The list of tasks.
    """
    if not tasks:
        print("No tasks yet – time to add some! 📝")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main demo - Run this to see all functions in action
if __name__ == "__main__":
    print("=== Function Examples and To-Do Demo ===")
    
    # Example 1
    greet_the_world()
    
    # Example 2
    sum_result = add_two_numbers(5, 3)
    print(f"Stored sum: {sum_result}")
    
    # Example 3
    greeting = personalized_greeting("Alex", "evening")
    print(greeting)
    
    # Example 4
    bmi_val, bmi_cat = calculate_bmi(70, 1.75)
    print(f"Your BMI is {bmi_val}: {bmi_cat}")
    
    # Small Project Demo
    my_tasks = []
    my_tasks = add_task(my_tasks, "Learn Python functions")
    my_tasks = add_task(my_tasks, "Build a GitHub repo")
    list_tasks(my_tasks)
    
    print("=== Functions Make Life Easier! ===")
    print("*"*40)
    print("\nLearn with Sithum")
