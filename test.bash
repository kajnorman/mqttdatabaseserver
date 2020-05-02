echo "showing live mqttdata 10 secs"
timeout 10 python3 mqttdatabaseserver.py
echo "inserting one line in database and displaying all data"
bash displaysqlitedata.bash
