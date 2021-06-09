import random;

# 1. 시나리오
## 숫자 6개(1~45) 입력
## 당첨 번호는 1~45까지 랜덤하게 함수로 번호 생성
## 맞춘 개수로 등수를 정합니다. 즉, 0개 : 7등, 1개 : 6등 ~~ 6개 : 1등입니다.
## 상금은 1000원~10000원 사이 랜덤으로 생성
## 상금 배분 비율은 1등 : 50%, 2등 : 30%, 3등 : 10%, 4등 : 5%, 5등 : 3%, 6등 : 2%, 7등 : 0%

# 2.
def lotto():
    money = [];
    temp_l = [0.5, 0.3, 0.1, 0.05, 0.03, 0.02]
    num = random.sample(range(1, 7), 6);

    temp = random.randint(1000, 10000);
    for i in temp_l:
        money.append(temp * i);
    money.sort();
    return num, money;

while True:
    cnt = 0;
    my_num = [];
    a = lotto();

    my_num = input('1~45까지의 번호 중 6개를 적으세요. ').split();
    my_num = [int(i) for i in my_num];

    for i in a[0]:
        for j in my_num:
            if i == j:
                cnt += 1;
    print('맟춘갯수 : ', cnt);

    if cnt == 0:
        print('등수 : 7등', '0 원')
    elif cnt == 1:
        print('등수 : 6등', a[1][0], '원');
    elif cnt == 2:
        print('등수 : 5등', a[1][1], '원');
    elif cnt == 3:
        print('등수 : 4등', a[1][2], '원');
    elif cnt == 4:
        print('등수 : 3등', a[1][3], '원');
    elif cnt == 5:
        print('등수 : 2등', a[1][4], '원');
    elif cnt == 6:
        print('등수 : 1등', a[1][5], '원');

    retry = input('다시 시작하시겠습니까? Y ');
    if retry == 'Y' or retry == 'y':
        continue;

    else: break;