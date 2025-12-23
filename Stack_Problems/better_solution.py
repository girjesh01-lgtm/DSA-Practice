def validate_parentheses(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if stack and pairs[ch] == stack[-1]:
                stack.pop()
            else:
                return False


    return len(stack) == 0


str = "()[]{}"
print(validate_parentheses(str))
