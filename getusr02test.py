# This example shows how to retrieve data from SAP R/3.
# It also shows how to extend structure obtained from SAP system with custom fields.
# -*- coding: utf-8 -*-
# This example needs connection to SAP R/3 system.

# This example is basically the same as example3.py but it uses data conversion routine to
# translate inverted date to 'normal' date instead of using additional table.
import pysap
import time
import sys
import MySQLdb
import datetime


'''def inv_to_date(obj,inv_date):
    # Small function to convert SAPs inverse date to 'normal' date
    dat=99999999-int(inv_date)
    year,day=divmod(dat,100)
    year,month=divmod(year,100)
    return time.strftime(pysap.RFC_DATE_FORMAT,(year,month,day,0,0,0,0,0,0))'''
# define system and date
sys_id = ['YD1', 'D11']
today = time.strftime('%Y%m%d', time.localtime(time.time()))
# Change next line to be able to connect to your SAP system
sap_conn = pysap.Rfc_connection(
    conn_file='E:\Repos\mycode\sapconn.ini', conn_name='%s' % sys_id[1])

# mysql connection
conn = MySQLdb.connect(
    host='10.0.1.105',
    port=5029,
    user='root',
    passwd='test!',
    db='BH_RSI_Repository',
)
cur = conn.cursor()

# open SAP connection
sap_conn.open()
# Read at most 20 entries from TCURR for AUD and exchange rate type 'M'

itab_usr02 = sap_conn.read_table('USR02', options=[
                                 "USTYP eq 'A' and ", "MANDT eq '112'"], max_rows=10)
for i in itab_usr02:
    print i['GLTGB']+"i"
# Set (output) conversion routine for field 'gdatu'
# itab_usr02.struc.set_conversion('gdatu',out_conv=inv_to_date)
# Create sort function for the table
# Sort by date (gdatu) using its int_value (inverted date) in ascending order
# sort_fnc=pysap.create_sort_func(('BNAME','GLTGB',1))
# Sort table
# itab_usr02.sort(sort_fnc)
# Print data (table lines act like dictionaries using field names as keys)
'''title='BNAME     |GLTGV     |GLTGB     |USTYP     |ANAME'
print title'''
sap_conn.close()

'''for l in itab_usr02:
    print  '%(BNAME)s%(GLTGV)10s|%(GLTGB)10s|%(USTYP)10s|%(ANAME)15s|%(ERDAT)10s|\
%(TRDAT)10s|%(LTIME)10s' % l'''


# create table
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
# print '%(BNAME)s' % itab_usr02[0]
# insert data


for l in itab_usr02:
    cur.execute("insert into `test`.`SAPAccountAudit` (`usercode`,`valid_from`,`Valid_to`,\
`type`,`creator`,`create_on`,`Last_logon_d`,`Last_logon_t`,`inputdate`,`sid`) values ('%(BNAME)s','%(GLTGV)s',\
    '%(GLTGB)s','%(USTYP)s','%(ANAME)s','%(ERDAT)s','%(TRDAT)s','%(LTIME)s'," % l + "'%s','%s')" % (today, sys_id[0]))


# update data
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

# delete data
#cur.execute("delete from student where age='9'")

# select data
'''cur.execute("SELECT COUNT(DISTINCT usercode) FROM `test`.`SAPAccountAudit` WHERE inputdate = '2016-10-31' AND diffdays > 30")
results=cur.fetchall()
for res in results:
    print res[0]'''
cur.close()
conn.commit()
conn.close()
