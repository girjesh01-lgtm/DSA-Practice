def validate_parentheses(s):
    stack = []

    for element in s:
        if element == '(':
            stack.append(element)
            continue
        elif element == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            else:
                return False

        elif element == '{':
            stack.append(element)
            continue
        elif element == '}':
            if stack and stack[-1] == '{':
                stack.pop()
                continue
            else:
                return False

        elif element == '[':
            stack.append(element)
            continue
        elif element == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                continue
            else:
                return False


    if stack:
        return False
    else:
        return True



str = "()[]{}{"
print(validate_parentheses(str))