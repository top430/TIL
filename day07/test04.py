st = ['id', 'pwd', 'name'];
data = ['id01','pwd01','james',30];

cust = zip(st,data);
print(cust);

for s,d in cust:
    print('%s : %s' % (s,d));