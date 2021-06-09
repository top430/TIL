def flunk(s):
    return s<60;

score = [40,80,50,70,90];
new_score = [];

for s in filter(flunk, score):
    