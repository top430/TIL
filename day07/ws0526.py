import csv;

f = None;
l_2020 = [];
list1 = [];

try:
    f = open('ta_2020.csv');
    data = csv.reader(f);
    for row in data:
        row[2]=float(row[2]);
        l_2020.append(row);


except:
    print('File Not Found...');
finally:
    if f != None:
        f.close();

i = c = avg = 0;
v=[];
k=[];
l=[];
#print(l_2020[0][0])

l_2020 = [['a123','b123'], ['c123','d123'], ['e123','f123']]

for i in range(len(l_2020)):
    for j in l_2020[i][0]:
        v.append(j)
print(v)

for i in l:
    if i[5:7] == '01':
        p = cnt = 0;
        for temp in k:
            p += temp;
            cnt+=1;
            #print(p)

#elif a[5:7] == '02':
