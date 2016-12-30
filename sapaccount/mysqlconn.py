import MySQLdb



# connection parameter to MySQL
conn = MySQLdb.connect(
    host='10.0.1.105',
    port=5029,
    user='test',
    passwd='test!',
    db='BH_RSI_Repository',
)