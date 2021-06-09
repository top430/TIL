class WeatherSql:
    make_weatherdb = ''' CREATE  TABLE  IF NOT EXISTS WeatherDB (
        ID  INTEGER PRIMARY KEY AUTOINCREMENT,
        CITY  TEXT,
        PROVINCE TEXT,
        DATE TEXT,
        WEATHER TEXT,
        TMAX REAL,
        TMIN REAL
    ) ''';
    insert_weatherdb = ''' INSERT  INTO  WeatherDB( CITY,PROVINCE, DATE, WEATHER, TMAX, TMIN) VALUES (?,?,?,?,?,?) ''';
    select_weatherdb_tmx = ''' SELECT  TMAX  FROM  WeatherDB  WHERE CITY=? ''';
    select_weatherdb_tmn = ''' SELECT  TMIN  FROM  WeatherDB  WHERE CITY=? ''';
    select_weatherdb_city = ''' SELECT  CITY  FROM  WeatherDB  ''';