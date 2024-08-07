import math


def prec(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/' or op == '%':
        return 2
    return 0

def func(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '%':
        de = a - math.floor(a) + b - math.floor(b)
        if  de:
            print("The operands for '%' should be integers.")
            exit()
        else:
            return a % b

def evaluate(expression):

    chars = list(expression)

    value = []

    ops = []

    i = 0

    while i < len(chars):
        if chars[i] == '(':
            ops.append(chars[i])
        elif chars[i].isdigit():
            val = 0
            while (i < len(chars) and (chars[i].isdigit() or chars[i] == '.')):
                if chars[i].isdigit():
                    val = (val * 10) + int(chars[i])
                    i += 1
                elif chars[i] == '.':
                    i += 1
                    decimal = 0.1
                    while (i < len(chars) and chars[i].isdigit()):
                        val += int(chars[i]) * decimal
                        decimal /= 10
                        i += 1
            value.append(val)
            i -= 1
        elif chars[i] == ')':
            while ops[-1] != '(':
                val2 = value.pop()
                val1 = value.pop()
                op = ops.pop()
                value.append(func(val1, val2, op))
            ops.pop()
        elif chars[i] == '-':
            if i == 0 or chars[i-1] in ['+', '-', '*', '/', '%', '(']:
                value.append(-1)
                ops.append('*')
                # val = 0
                # i += 1
                # while (i < len(chars) and chars[i].isdigit() or chars[i] == '.'):
                #     if chars[i].isdigit():
                #         val = (val * 10) + int(chars[i])
                #     elif chars[i] == '.':
                #         i += 1
                #         decimal = 0.1
                #         while (i < len(chars) and chars[i].isdigit()):
                #             val += int(chars[i]) * decimal
                #             decimal /= 10
                #             i += 1
                #         i -= 1
                #     i += 1
                #         # val = (val * 10) + int(chars[i])
                #         # i += 1
                # value.append(-val)
                # i -= 1
            # elif chars[i+1] == '(':
            #     value.append(-1)
            #     ops.append('*')
        else:
            while (len(ops) != 0 and prec(ops[-1]) >= prec(chars[i])):
                val2 = value.pop()
                val1 = value.pop()
                op = ops.pop()
                value.append(func(val1, val2, op))
            ops.append(chars[i])
        i += 1

    while len(ops) != 0:
        val2 = value.pop()
        val1 = value.pop()
        op = ops.pop()
        value.append(func(val1, val2, op))

    return value[-1]

expression = input("Enter the expression: ").replace(" ", "")

valid_chars = set('0123456789+-*/%().')
if not all(char in valid_chars for char in expression):
    print("Invalid input")
else:
    print(evaluate(expression))
