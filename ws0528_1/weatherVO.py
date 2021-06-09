class WeatherVO:
    def __init__(self,city,province,date,weather,tmx,tmn):
        self.__city = city;
        self.__province = province;
        self.__date =date;
        self.__weather= weather;
        self.__tmx = tmx;
        self.__tmn = tmn;

    def __str__(self):
        return "(%s)%s 지역의 %s %s %f %f" %(self.__province, self.__city, self.__date, self.__weather, self.__tmx, self.__tmn);

    def getCity(self):
        return self.__city;
    def setCity(self,city):
        self.__city = city;

    def setProvince(self,province):
        self.__province = province;
    def getProvince(self):
        return self.__province;

    def getDate(self):
        return self.__date;
    def setDate(self,date):
        self.__date = date;
    def getWeather(self):
        return self.__weather;
    def setWeather(self,weather):
        self.__weather = weather;
    def getTmx(self):
        return self.__tmx;
    def setTmx(self,tmx):
        self.__tmx = tmx;
    def getTmn(self):
        return self.__tmn;
    def setTmn(self,tmn):
        self.__tmn = tmn;