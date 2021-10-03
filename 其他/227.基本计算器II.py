def calculate(strA: str):
    stack = []
    pre_op = "+"
    num = 0
    for i, each in enumerate(strA):
        if each.isdigit():
            num = num * 10 + int(each)
        if i == len(strA) - 1 and each in "+-*/":
            if pre_op == "+":
                stack.append(num)
            elif pre_op == "-":
                stack.append(-num)
            elif pre_op == "*":
                stack.append(stack.pop() * num)
            elif pre_op == "/":
                top = stack.pop()
                if top < 0:
                    stack.append(int(top / num))
                else:
                    stack.append(top // num)
            pre_op = each
            num = 0
    return sum(stack)