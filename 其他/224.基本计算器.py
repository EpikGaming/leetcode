def calculate(strA: str):
    res, num, sign = 0, 0, 1
    stack = []
    for s in strA:
        if s.isdigit():
            num = 10 * num + int(s)
        elif s == "+" or s == "-":
            res += sign * num
            num = 0
            sign = 1 if s == "+" else -1
        elif s == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif s == ")":
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    res += sign * num
    return res


test = "(2+3)-(1-4)+(3-2)"
print(calculate(test))