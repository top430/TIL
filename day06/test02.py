import random
# 당첨금은 랜덤하게 만든다.
# 당첨 번호는 랜덤하게 만든다.
# 순위에 따라 당첨금을 차등 지급 한다.
# 게임을 끝내고 다시 시작 할 수 있다.
# 함수를 이용한다.

# lotto 번호 생성함수
def lotto():
    temp = [];
    for i in range(0,6):
        ran = random.randint(1, 45);
        if ran not in temp:
            temp.append(ran);
    return temp
l = lotto();

print(l);
prize = random.randint(1000, 10000);    # 상금 랜덤 생성

# 내 숫자 6개 입력
my_num = [];
for n in range(0,6):    # 여섯 숫자 한꺼번에 넣는 걸로 변경
    num = int(input('Input number...(1~45)?'));
    my_num.append(num);
print(my_num);

# 맞힌 숫자 개수
cnt = 0;
for a in l:
    for b in my_num:
        if a == b:
            cnt += 1;
print(cnt);

if cnt == 6:
    print('1등입니다. 당첨금은 %d입니다.' % (prize * 0.5));
elif cnt == 5:
    print('5개 + 보너스 숫자 2등입니다. 당첨금은 %f입니다.' % (prize * 0.3));
elif cnt == 4:
    print('5개 맞추면 3등입니다. 당첨금은 %f입니다.' % (prize * 0.1));
elif cnt == 3:
    print('4등 당첨금은 %f입니다.' % (prize * 0.05));
elif cnt == 2:
    print('5등 당첨금은 %f입니다.' % (prize * 0.03));
elif cnt == 1:
    print('6등 당첨금은 %f입니다.' % (prize * 0.02));
