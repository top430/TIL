score = [
    ['2019-01-03', 10, 12, 14, 10],
    ['2020-02-03', 12, 12, 14, 11],
    ['2020-03-03', 13, 13, 15, 12],
    ['2020-03-04', 14, 14, 16, 13],
    ['2020-04-03', 15, 15, 17, 14],
];

#각 측정 데이터 별 평균 온도

for a in range(len(score)):
    sum = cnt = 0;
    for i in range(1, len(score[a])):
        sum += score[a][i];
        cnt += 1;
    print(score[a][0], sum/cnt);

print('');
#2020년 온도 평균
cnt = sum = 0
for a in range(len(score)):
    for i in range(1, len(score[a])):
        if '2020' in score[a][0][0:4]:
            sum += score[a][i];
            cnt += 1;
print('2020년', sum/cnt)

print('');
#2020년 월평균 온도
sum_02 = sum_03 = sum_04 = cnt_02 = cnt_03 = cnt_04= 0
for a in range(len(score)):
    if '2020-02' in score[a][0][0:8]:
        for i in range(1, len(score[a])):
            sum_02 += score[a][i];
            cnt_02 += 1;
    elif '2020-03' in score[a][0][0:8]:
        for i in range(1, len(score[a])):
            sum_03 += score[a][i];
            cnt_03 += 1;
    elif '2020-04' in score[a][0][0:8]:
        for i in range(1, len(score[a])):
            sum_04 += score[a][i];
            cnt_04 += 1;
print('2020년 2월', sum_02/cnt_02);
print('2020년 3월', sum_03/cnt_03);
print('2020년 4월', sum_04/cnt_04);

print('');
#2020년 일평균 최고기온과 최저기온의 차
max_02 = max_03 = max_04 = 0
min_02 = min_03 = min_04 = 20
for a in range(len(score)):
    if '2020-02' in score[a][0][0:8]:
        for i in range(1, len(score[a])):
            if max_02 <= score[a][i]:
                max_02 = score[a][i];
            if min_02 >= score[a][i]:
                min_02 = score[a][i];
    if '2020-03' in score[a][0][0:8]:
        for i in range(1, len(score[a])):
            if max_03 <= score[a][i]:
                max_03 = score[a][i];
            if min_03 >= score[a][i]:
                min_03 = score[a][i];
    if '2020-04' in score[a][0][0:8]:
        for i in range(1, len(score[a])):
            if max_04 <= score[a][i]:
                max_04 = score[a][i];
            if min_04 >= score[a][i]:
                min_04 = score[a][i];
print('2월',max_02-min_02); print('3월',max_03-min_03); print('4월',max_04-min_04);