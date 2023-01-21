from stack import Stack

def reverseString(stack, str):
    for i in range(len(str)):
        stack.push(str[i])
    rev_str = ''

    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str


s = Stack()
sentence ="lets be friends!"
print(reverseString(s, sentence))
