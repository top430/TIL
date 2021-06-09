import sqlite3
from weatherSql import WeatherSql

class WeatherDB:
    def __init__(self, db):
        self.__db = db;

    def getConn(self):
        con = sqlite3.connect(self.__db);
        cursor = con.cursor();
        return {'con':con,'cursor':cursor};

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();

    def makeTable(self):
        cc = self.getConn();
        cc['cursor'].execute(WeatherSql.make_weatherdb);
        cc['con'].commit();
        self.close(cc);

    def insert(self,weather):
        cc = self.getConn();
        cc['cursor'].execute(WeatherSql.insert_weatherdb, (weather.getCity(),weather.getProvince(),weather.getDate(), weather.getWeather(), weather.getTmx(), weather.getTmn() ));
        cc['con'].commit();
        self.close(cc);
        print("등록완료.")

    def selectTmx(self,city):
        cc = self.getConn();
        cc['cursor'].execute(WeatherSql.select_weatherdb_tmx,(city,));
        objs = cc['cursor'].fetchall();
        self.close(cc);
        tmxs =[];
        for o in objs:
            tmxs.append(o[0]);
        return tmxs;

    def selectTmn(self,city):
        cc = self.getConn();
        cc['cursor'].execute(WeatherSql.select_weatherdb_tmn,(city,));
        objs = cc['cursor'].fetchall();
        self.close(cc);
        tmns=[];
        for o in objs:
            tmns.append(o[0]);
        return tmns;

    def selectCity(self):
        cc= self.getConn();
        cc['cursor'].execute(WeatherSql.select_weatherdb_city);
        objs = cc['cursor'].fetchall();
        self.close(cc);
        citys =[];
        for c in objs:
            if c[0] not in citys:
                citys.append(c[0]);
        return citys;