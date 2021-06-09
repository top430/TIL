st1 = 'abcdef';

print(type(st1));
print(len(st1));

print(st1[-2]);

for c in st1:
    print(c, end=',');

print()

for i in range(0, len(st1)): # 0, 6
    print(st1[i], end=',');
print()

st2 = '2021-05-21';
print(st2[0:4]);
print(st2[5:7]);
print(st2[-2:]);

st3 = 'flower.jpg';
print(st3[:-4]);

st4 = '월화수목금토일';
st5 = st4[::-1]
print(st4);
print(st5);