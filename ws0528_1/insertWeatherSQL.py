from urllib import request
import bs4
from weatherDB import WeatherDB
from weatherVO import WeatherVO

print ("start");
wdb = WeatherDB('weathers');
wdb.makeTable();

target = request.urlopen('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108');
soup = bs4.BeautifulSoup(target,'html.parser');

for st in soup.select("location") :
    province = (st.select_one('province').string);
    city = st.select_one('city').string;
    for data in st.select('data'):
        tmEf = data.select_one('tmEf').string;
        wf = data.select_one('wf').string;
        tmn =float(data.select_one('tmn').string);
        tmx =float(data.select_one('tmx').string) ;

        wt = WeatherVO(city, province, tmEf, wf, tmx, tmn);
        wdb.insert(wt);