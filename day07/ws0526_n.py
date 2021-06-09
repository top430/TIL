import csv;

f = open('ta_2020.csv');
data = csv.reader(f);

temp = [0,0,0,0,0,0,0,0,0,0,0,0];
date = [0,0,0,0,0,0,0,0,0,0,0,0];

for day in data :
    for i in range(0, 12):
        if int(day[0][day[0].find('-')+1:day[0].rfind('-')]) == i+1:
            temp[i] += float(day[2]);
            date[i] += 1;

temp_avg = [];
for c in range(0,12) :
    temp_avg.append(round(temp[c] / date[c], 2));
print(temp_avg);
