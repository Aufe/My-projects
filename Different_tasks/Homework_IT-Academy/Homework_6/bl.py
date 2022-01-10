import data

def calculate_expression(expression):
    validate = validation(expression)
    if not validate:
        return "Incorrect input"
    tokens = sort_tokens(sort_expression(expression))
    stack_numbers = []
    stack_operations = []
    for el in tokens:
        if isinstance(el, float):
            stack_numbers.append(el)
        elif el == "(":
            stack_operations.append(el)
        elif el in data.operators.keys():
            if not stack_operations or stack_operations[-1] == "(":
                stack_operations.append(el)
            else:
                if data.operators[el][0] > data.operators[stack_operations[-1]][0]:
                    stack_operations.append(el)
                else:
                    while stack_operations and stack_operations[-1] != "(" and data.operators[el][0] <= data.operators[stack_operations[-1]][0]:
                        y, x = stack_numbers.pop(), stack_numbers.pop()
                        token = data.operators[stack_operations[-1]][1](x, y)
                        stack_operations.pop()
                        stack_numbers.append(token)
                    stack_operations.append(el)
        else:
            while stack_operations[-1] != "(":
                y, x = stack_numbers.pop(), stack_numbers.pop()
                token = data.operators[stack_operations[-1]][1](x, y)
                stack_operations.pop()
                stack_numbers.append(token)
            stack_operations.pop()
    while stack_operations:
        y, x = stack_numbers.pop(), stack_numbers.pop()
        token = data.operators[stack_operations[-1]][1](x, y)
        stack_operations.pop()
        stack_numbers.append(token)
    return stack_numbers[0]

def sort_expression(expression):
    tokens = []
    number = ""
    _one = 1
    for i in range(len(expression)):
        if expression[i] in ".0123456789":
            number += expression[i]
        elif number:
            tokens.append(float(number) * _one)
            _one = 1
            number = ""
        if expression[i] in data.operators.keys() or expression[i] in "()":
            if expression[i] == "-" and (i == 0 or expression[i - 1] == "("):
                _one *= -1
                continue
            tokens.append(expression[i])
    if number:
        tokens.append(float(number))
    return tokens

def sort_tokens(tokens): # if the expression has "(-number)"
    for i in range(1, len(tokens) - 1):
        if isinstance(tokens[i], float) and tokens[i - 1] == "(" and tokens[i + 1] == ")":
            tokens.pop(i + 1)
            tokens.pop(i - 1)
            return sort_tokens(tokens)
    return tokens

def validation(expression):
    open_parenthesis = 0
    closing_parenthesis = 0
    stack = []
    for el in expression: 
        if el == "(":
            open_parenthesis += 1
        elif el == ")":
            closing_parenthesis += 1
        elif el not in ".0123456789 ()" and el not in data.operators.keys():
            return False
        stack.append(el)
        if len(stack) > 1:
            if stack[-1] in data.operators.keys() and stack[-2] in data.operators.keys():
                return False
            elif stack[-1] in data.operators.keys() and stack[-1] != "-" and stack[-2] == "(":
                return False
            elif stack[-1] == "(" and (stack[-2] not in data.operators.keys() and stack[-2] not in "("):
                return False
            elif stack[-2] == ")" and (stack[-1] not in data.operators.keys() and stack[-1] not in ")"):
                return False
    return open_parenthesis == closing_parenthesis
