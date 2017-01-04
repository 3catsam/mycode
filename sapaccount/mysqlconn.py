'''import MySQLdb



# connection parameter to MySQL
conn = MySQLdb.connect(
    host='10.0.1.105',
    port=5029,
    user='test',
    passwd='test!',
    db='test',
)
'''
import pymysql.cursors
 
# Connect to the database
conn = pymysql.connect(
    host='10.0.1.105',                         
    port=5029,
    user='test',
    password='test!',
    db='test',
    charset='gbk',
    cursorclass=pymysql.cursors.DictCursor
)