def is_paranthesis(s):
    stack = []
    bracket_map =  {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if stack  and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
    return not stack #or len(stack) == 0

print(is_paranthesis("[{}]"))
