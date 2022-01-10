import bl

def show_query(message):
    return input(format_message(message, ":\n"))

def show_message(message, end):
    print(format_message(message, end))

def format_message(message, end):
    return f"{message}{end}"

def calculate_expression():
    expression = show_query("Enter the expression, please")
    show_message(bl.calculate_expression(expression), "!")

def main_flow():
    while True:
        choise = show_query("Please, select the operation (calculate expression, exit)")
        if choise == "calculate expression":
            calculate_expression()
            continue
        elif choise == "exit":
            break
        else:
            show_message("Incorrect input, try again", ".")
            continue

if __name__ == "__main__":
    main_flow()