# 1. 시나리오
## 숫자 6개 입력, 1~45까지 랜덤하게 숫자

# 2. 전제 조건
## - 당첨금은 랜덤하게 만든다.
## - 당첨 번호는 랜덤하게 만든다.
## - 순위에 따라 당첨금을 차등 지급 한다.
## - 게임을 끝내고 다시 시작 할 수 있다.
## - 함수를 이용한다.
import random

# 자동 번호 생성기
def num_c() :
    num6 = []
    for i in range(0, 6):
        num = random.randint(1, 46);
        num6.append(num);
    return num6;

# 당첨금
def money() :
    cnt = range(0, 8)
    mon7 = [0]
    for i in range(0, 6) :
        mon = random.randint(1, 10000);
        mon7.append(mon);
    mon7.sort();
    d = dict(zip(cnt, mon7));
    return d;

# 게임 시작
while True :
    cnt = 0;
    user = input('6개의 숫자를 입력하시오(1~45)(종료 : q) : ').split();
    num_r = num_c();
    if user[0] == 'q':
        break;
    else:
        for i in user:
            print(i);
        num_u = [int(i) for i in user];
        print(num_u);
        for i in range(0, 6) :
            if num_u[i] == num_r[i] :
                cnt += 1;
    win = money();
    result = win[cnt];
    print('%d개 맞추셔서 당첨금은 %d원입니다.' % (cnt, result));
