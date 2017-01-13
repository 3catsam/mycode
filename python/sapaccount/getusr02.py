#coding:utf-8
# This example shows how to retrieve data from SAP R/3.
# It also shows how to extend structure obtained from SAP system with custom fields.
# This example needs connection to SAP R/3 system.

# This example is basically the same as example3.py but it uses data conversion routine to
# translate inverted date to 'normal' date instead of using additional table.
import pysap
import time
import sys
import os
import MySQLdb
import datetime
from mysqlconn import conn


#sys_id = ['EP1', 'P11','P31','P41','P91']
sys_id = ['D11', 'YD1']
# set inputdata parameter
today = time.strftime('%Y%m%d', time.localtime(time.time()))
# print today
# find current directory


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

base_dir = cur_file_dir()

# connection parameter to MySQL
'''conn = MySQLdb.connect(
    host='10.0.1.105',
    port=5029,
    user='root',
    passwd='test!',
    db='BH_RSI_Repository',
)'''
# Loops of all SAP SID
for i in sys_id:
    sap_conn = pysap.Rfc_connection(
        conn_file=r'%s/sapconn.ini' % base_dir, conn_name=r'%s' % i)
    cur = conn.cursor()
    sap_conn.open()
    itab_usr02 = {}
    itab_usr02x = {}
    # get valid user from sap.usr02:
    # get data from sap.usr02 for no limited users

    itab_usr02 = sap_conn.read_table('USR02', options=[
        "USTYP eq 'A' and GLTGB eq '00000000'"], fields=['BNAME', 'GLTGV', 'GLTGB', 'USTYP',
                                                         'ANAME', 'ERDAT', 'TRDAT', 'LTIME'], max_rows=9999)
    # get data from sap.usr02 for limited users
    itab_usr02x = sap_conn.read_table('USR02', options=[
        "USTYP eq 'A' and GLTGB gt '%s'" % today], fields=['BNAME', 'GLTGV', 'GLTGB', 'USTYP',
                                                           'ANAME', 'ERDAT', 'TRDAT', \
                                                           'LTIME'], max_rows=9999)

    # close saprfc
    sap_conn.close()
    # input data to mysql.SAPAccountAudit
    # unlimited users:
    #
    for l in itab_usr02:
        cur.execute("insert into `test`.`SAPAccountAudit` (`usercode`,`valid_from`,`Valid_to`,\
`type`,`creator`,`create_on`,`Last_logon_d`,`Last_logon_t`,`inputdate`,`sid`) values ('%(BNAME)s','%(GLTGV)s',\
    '%(GLTGB)s','%(USTYP)s','%(ANAME)s','%(ERDAT)s','%(TRDAT)s','%(LTIME)s'," % l + "'%s','%s')" % (today, i))
    # limited users:
    for l in itab_usr02x:
        cur.execute("insert into `test`.`SAPAccountAudit` (`usercode`,`valid_from`,`Valid_to`,\
`type`,`creator`,`create_on`,`Last_logon_d`,`Last_logon_t`,`inputdate`,`sid`) values ('%(BNAME)s','%(GLTGV)s',\
    '%(GLTGB)s','%(USTYP)s','%(ANAME)s','%(ERDAT)s','%(TRDAT)s','%(LTIME)s'," % l + "'%s','%s')" % (today, i))
# update new data(inputdate==today):
# islogon means active user
# update flag islogon=true when lastlogon is not null or create date less
# than 90 days.
cur.execute("UPDATE `test`.`SAPAccountAudit` SET islogon = TRUE WHERE inputdate = '%s' \
AND `Last_logon_d` <> '0000-00-00' OR DATEDIFF(inputdate, create_on) <= 90" % today)
# update diffdays = 1 when create date less than 90 days and haven't logoned system.
# we should make sure it's a vilid user.
cur.execute("UPDATE `test`.`SAPAccountAudit` SET diffdays = 1 WHERE inputdate = '%s' AND \
islogon = TRUE AND `Last_logon_d` = '0000-00-00'" % today)
# set invalid users' diffdays = 100.
cur.execute("UPDATE `test`.`SAPAccountAudit` SET diffdays = 100 WHERE inputdate = '%s' AND \
islogon = FALSE" % today)
# count vilid users' diffdays.WARN:'1' and '100' are special value.
cur.execute("UPDATE `test`.`SAPAccountAudit` SET diffdays = DATEDIFF(inputdate, Last_logon_d) \
WHERE inputdate = '%s' AND islogon = TRUE AND `Last_logon_d` <> '0000-00-00'" % today)
# update users' corp_name,user_name from ODM,only newly inputed data.
# update corp_name of AGT where sid = P91
cur.execute("UPDATE `test`.`SAPAccountAudit` SET `CORP_NAME` = 'AGT' WHERE sid = 'P91' AND \
inputdate = '%s'" % today)
cur.execute("UPDATE `test`.`SAPAccountAudit` a INNER JOIN `BH_RSI_Repository`.`ODM` b \
ON a.`usercode`=b.`USER_CODE` SET a.`CORP_NAME` = b.`CORP_NAME` where a.inputdate = '%s' and b.`CORP_NAME`\
IS NOT NULL" % today)
cur.execute("UPDATE `test`.`SAPAccountAudit` a INNER JOIN `BH_RSI_Repository`.`ODM` b \
ON a.`usercode`=b.`USER_CODE` SET a.`USER_NAME` = b.`USER_NAME` where a.inputdate = '%s' and b.`USER_NAME` \
IS NOT NULL" % today)
# refresh the active users
cur.execute("INSERT INTO `test`.`tmp_SAPAccountAudit`(`usercode`,`mindiffdays`) SELECT `usercode`,\
MIN(`diffdays`) FROM `test`.`SAPAccountAudit` WHERE `inputdate` = '%s' GROUP BY `usercode`" % today)
cur.execute("UPDATE `test`.`SAPAccountAudit` a INNER JOIN `test`.`tmp_SAPAccountAudit` b \
ON a.`usercode`= b.`usercode` SET a.`diffdays`=b.`mindiffdays` WHERE a.`inputdate` = '%s'" % today)
cur.execute("TRUNCATE TABLE `test`.`tmp_SAPAccountAudit`")
cur.close()
conn.commit()
conn.close()
