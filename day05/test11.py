a = 24242.4322
cnt = 0;

score = [
    [90,80,100,92],
    [91,81,100,91],
    [92,82,100,92],
    [90,80,100,93],
    [90,80,100,94],
]
sum2 = 0

#합
for i in score:
    sum = 0

    for j in i:
         sum += j;

    #print(sum);


#전체 합

for i in score:
    for j in i:
        print(score, end = '')

print(sum2);

print(sum2/len(score))

print('%.9f' % a)