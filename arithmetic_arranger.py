def arithmetic_arranger(problems, condition=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    top = ''
    bottom = ''
    lines = ''
    totals = ''

    for i in problems:
        FirstNum = i.split()[0]
        operator = i.split()[1]
        SecondNum = i.split()[2]
        if operator == '/' or operator == '*':
            return 'Error: Operator must be '+' or '-'.'
        if len(FirstNum) > 4 or len(SecondNum) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not FirstNum.isdigit() or not SecondNum.isdigit():
            return 'Error: Numbers must only contain digits.'
        

        if operator == '+':
            total = int(FirstNum) + int(SecondNum)
        else:
            total = int(FirstNum) - int(SecondNum)
        
        OperatorDist = max(len(FirstNum), len(SecondNum)) + 2
        SecondNum = operator + SecondNum.rjust(OperatorDist - 1)
        top += FirstNum.rjust(OperatorDist) + (4 * ' ')
        bottom += SecondNum + (4 * ' ')
        lines += len(str(SecondNum)) * '-' + (4 * ' ')
        totals += str(total).rjust(OperatorDist) + (4 * ' ')
        if condition:
            arranged_problems = top + '\n' + bottom + '\n' + lines + '\n' + totals
        else:
            arranged_problems = top + '\n' + bottom + '\n' + lines
    return arranged_problems

        
if __name__ == '__main__':
    print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
        



    