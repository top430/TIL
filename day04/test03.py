# 함수명: calc
# 숫자 2개와 연산자(+,-,/,*) 3개를 함수로 전달하여 결과를 return하는 함수를 구현하시오

def calc(n1, op, n2):
    result = 0;
    if op == '+':
        result = n1 + n2;
    elif op == '-':
        result = n1 - n2;
    elif op == '/':
        result = n1 / n2;
    elif op == '*':
        result = n1 * n2;
    else:
        result = '다시입력하세요'

    return result;

num1 = input('Input num1 ...');
num2 = input('input num2 ...');
op = input('Input op...');

data = calc(int(num1), op, int(num2));
print(data);