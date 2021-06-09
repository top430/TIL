
# 변수(valrial) 영역
data = 0;
num = 0;

# 함수(fuinction) 영역
def func():
    global num;
    num = 200;
    data = 100;
    return data;

# 코드 영역
result = func();
print(result);

rr = round(10.123123, 5);

print(rr)

stri = '1>2';
print(eval(stri));

intnum = int('100');
print(float('100'));

print(hex(10)); #16진수
print(oct(10)); #8진수
print(bin(10)); #2진수