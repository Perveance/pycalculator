#!/usr/local/bin/python3

import sys


def calc(val1, val2, op):

    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '*':
        return val1 * val2

def unwind(operators, operands):

    while len(operands) > 0 and len(operators) > 0:

        valr = int(operands.pop())
        vall = int(operands.pop())
        op = operators.pop()
        newval = calc(vall, valr, op)
        operands.append(newval)

def evaluate(expr):

    operators = []
    operands = []
    for c in expr:
        if c == ' ':
            continue
        elif c == '(':
            continue
        elif c == ')':
            unwind(operators, operands)
        elif c in ['+', '-', '*', '/']:
            operators.append(c)
        else:
            operands.append(c)

    unwind(operators, operands)

    return operands[0]

def valid(s):
    if len(s) == 0:
        return False

    # TODO: add more validations
    return True

def start():

    while True:

        print(">>", end=" ")
        sys.stdout.flush()
        expr = sys.stdin.readline().strip().lower()
        if (expr == "exit"):
            quit()
        if valid(expr):
            print(">> {0}".format(evaluate(expr.strip())))

def main():

    start()

main()
