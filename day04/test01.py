import random

def calc():
    a = 10
    b = 20
    result = a + b
    return result

sum = calc()
print(sum)

def rand_num():
    num = random.randint(1,10)
    return num

def calcsum(s):
    result = 0
    for i in range(1, 11):
        result += i;
    return result;

num = rand_num()
print(num)

sum2 = calcsum(5);
print(sum2)