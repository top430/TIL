import random
#숫자를 1개 입력받는다.
#1~9까지의 숫자만 입력받고 이외의 문자가 입력되면 다시 시도
#1~9까지의 숫자를 20개 Random하게 생성(중복허용)
#입력 받은 수가 몇개인지 갯수를 출력

cnt=0;

while True:
    a = input('숫자 입력 : ');
    if a.isnumeric():
        num = int(a);
        if num < 10:
            break;
        else: print('9이하의 숫자를 입력하세요.');
    else: print('숫자를 입력하세요.');

for i in range(20):
    rand = random.randint(1, 9);
    if rand == num:
        cnt += 1;

print('갯수:', cnt)
