def is_valid(s):
    # Create an empty stack to keep track of open brackets.
    stack = []
    
    # Create a mapping of closing brackets to their corresponding open brackets.
    mapping = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the input string 's'.
    for char in s:
        if char in mapping:
            # If the current character is a closing bracket, check if the stack is empty.
            # If it's not empty, pop the top element from the stack; otherwise, use '#' as a placeholder.
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element (the top element of the stack) matches
            # the corresponding open bracket for the current closing bracket 'char'.
            if mapping[char] != top_element:
                return False
        else:
            # If the current character is an open bracket, push it onto the stack.
            stack.append(char)

    # If the stack is empty at the end, it means all brackets were matched correctly.
    return not stack

# Example usage:

print(is_valid("()[]{}"))    # Output: True
