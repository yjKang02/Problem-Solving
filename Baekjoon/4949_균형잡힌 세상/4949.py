while(True):
    text = input()
    if text == '.': break
    queue = []
    answer = 'yes'
    for s in text:
        if s == '(' or s == '[':
            queue.append(')' if s == '(' else ']')
        elif s == ')' or s == ']':
            if len(queue) == 0 or queue[-1] != s:
                answer = 'no'
                break
            queue.pop()
    if len(queue) != 0: answer = 'no'
    print(answer)