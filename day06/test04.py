a = [1,2,3,4,5,6]
cnt = 0;
my_num = [4,5,7,1,2,3]

for i in a:
    for j in my_num:
        print(i, j)
        if i == j:
            cnt += 1;
print('맟춘갯수 : ', cnt);