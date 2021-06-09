def calc(*n):
    sum = 0;
    for i in n:
        sum += i;

    return sum/len(n);

r1 = calc(1,2);
r2 = calc(1,2,3,6);
print(r1);
print(r2);