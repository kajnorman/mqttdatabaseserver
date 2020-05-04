cd  data
sqlite3  data.db  <<STOP
select * from  full_table where ( key="trek/22/greenhouse/temperature");
STOP
