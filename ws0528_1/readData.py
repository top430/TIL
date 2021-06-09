from weatherDB import WeatherDB

print ("start");
wdb = WeatherDB('weathers');

# 지역 리스트 긁어오기
citylist = wdb.selectCity();

#각 지역 별 평균 온도들 구하기
for c in citylist:
    tmxs = wdb.selectTmx(c);
    tmns = wdb.selectTmn(c);

    tmx = sum(tmxs)/len(tmxs);
    tmn = sum(tmns)/len(tmns);
    print("%s 지역의 평균최저온도: %.2f도, 평균최고온도: %.2f도" %(c,tmn,tmx));