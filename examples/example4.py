# This examples shows how to perform remote function calls
# -*- coding: utf-8 -*-
# Connection to SAP R/3 system is needed for this example

import pysap
import sys
import ctypes
pysap.setSystemCodePage('8400')
# Modify next line to suit your connection details
sap_conn=pysap.Rfc_connection(conn_file='E:\Repos\mycode\sapconn.ini',conn_name="D11")
sap_conn.open()

# Create remote function interface
func=sap_conn.get_interface('RFC_GET_TABLE_ENTRIES')

# Print its description
print func.desc

# Fill the arguments needed
func['TABLE_NAME']='T001'
func['MAX_ENTRIES']=20

# Perform function call
# Only the arguments specified will be passed to SAP. This reduces bandwith.
# Note: Trying to access other parameters defined by 'RFC_GET_TABLE_ENTRIES'
# but not sent to SAP will raise SapRfcError
try:
    rc=func('TABLE_NAME','MAX_ENTRIES','ENTRIES')
except pysap.SapRfcError,desc:
    print "Error invoking 'RFC_GET_TABLE_ENTRIES': %s" % desc
else:
# Everything went well
# Now we have to translate received table ('ENTRIES') to the format of T001
# First create an internal table having structure of T001 as defined in DDIC
    itab=sap_conn.get_table('T001')
# Then copy rows of 'ENTRIES' to itab - this also converts rows structure on the fly
    itab.append_from_table(func['ENTRIES'])
# Using slicing above line could be rewritten as:
#itab[:]=func['ENTRIES']
# Print some fields from itab to show it worked
    for p in itab:
        print '%(BUKRS)5s %(BUTXT)-30s %(ORT01)-25s' % p
        
# Now let's get function module interface for BAPI
func=sap_conn.get_interface('BAPI_SALESORDER_GETLIST')

# Set the parameters (modify values to fit your system)
# Allthough 'CUSTOMER_NUMBER' is defined as CHAR, numerical values passed to it must be formatted as NUMC
func['CUSTOMER_NUMBER']='%010d' % 7315
func['SALES_ORGANIZATION']='0500'
func['DOCUMENT_DATE']='22.6.2001' # if mxDateTime is available
#func['DOCUMENT_DATE']='20010622' # use this instead if you don't have mxDateTime

# Perform function call
try:
    rc=func('CUSTOMER_NUMBER','SALES_ORGANIZATION','DOCUMENT_DATE','SALES_ORDERS','RETURN')
except pysap.SapRfcError,desc:
    print "Error invoking 'BAPI_SALESORDER_GETLIST': %s" % desc
else:
# Everything went ok - print the results (if any)
    for p in func['SALES_ORDERS']:
        print p
        
# Create structure using definition of VBAK from DDIC
# Structure contains only fields specified
s_vbak=sap_conn.get_structure('VBAK','vbeln','kunnr','erdat')
# Create an instance ...
tst=s_vbak()
# ... fill it with data ...
tst.from_list(('10029','1282','20030414'))
# ... and print it
print tst

# Close the connection before quiting
sap_conn.close()
print 'ok'
