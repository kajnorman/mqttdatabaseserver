cd  data
sqlite3  data.db  <<STOP
insert into full_table(reading_time ,key , value ) values (DATETIME('now'), "firsttstke","firstvalue");
select * from  full_table;
STOP
