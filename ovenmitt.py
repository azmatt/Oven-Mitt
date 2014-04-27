######Oven Mitt version 1.0
######Written in Python 2.7

import sqlite3
import datetime
import time

##HTML File Output Start
h = open('burner_hist.html', 'w')
h.write('<html><h2>Burner Information Report</h2>')


outside_num = 0; ## This is global variable

####################ZINBOUNDNUMBER Number Lookup Function

def ReturnOtherNumber( var_ron ):
	conn = sqlite3.connect('Burner.sqlite')
	c=conn.cursor()
	c.execute("SELECT * FROM ZINBOUNDNUMBER WHERE Z_PK=:Ph", {"Ph": var_ron})
	rows = c.fetchall()
	for row in rows:
		zent = row[0]
		str_zent = str(zent)
		onbr = row[10]
		str_other_number = str(onbr)
		outside_num = str_other_number
	
	return outside_num;

h.write('<p><b>Current Burner Numbers</b></p>')

conn = sqlite3.connect('Burner.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM ZBURNER")
rows = c.fetchall()
for row in rows:
	bmd = datetime.datetime(2001,1,1,0,0,0)
	zid = row[0]
	str_zid = str(zid)
	znum = row[25]
	str_znum = str(znum)
	raw_create = row[14]
	raw_expires = row[15]
	raw_update = row[16]
	nickname = row[17]
	real_create = bmd + datetime.timedelta(0,raw_create)
	real_expires = bmd + datetime.timedelta(0,raw_expires)
	real_update = bmd + datetime.timedelta(0,raw_update)
	h.write('Burner Number ID: ' + str_zid + '<br>')
	h.write( "Number Description: " + nickname + '<br>')
	h.write( "Burner Number: " + str_znum + '<br>')
	h.write( "Created Date: ")
	h.write( str(real_create) + '<br>' )
	h.write( "Expires On: ")
	h.write( str(real_expires) + '<br>')
	h.write( "Updated On: ")
	h.write( str(real_update) + '<br><br>')


conn = sqlite3.connect('Burner.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM ZBURNER ORDER BY Z_PK DESC LIMIT 1")
rows = c.fetchall()
for row in rows:
	zid = row[0]
	str_zid = str(zid)

h.write('<p><b>Incoming SMS messages</b></p>')
h.write('<table border="1">')
h.write('<tr><td><b>Date</b></td><td><b>From</b></td><td><b>Message</b></td></tr>')

conn = sqlite3.connect('Burner.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM ZCALLITEM ")
rows = c.fetchall()
for row in rows:

	if row[14] == "sms":
		rawtime = row[8]
		str_rawtime = str(rawtime)
		dfn = str_rawtime[:9] 
		int_dfn = int(dfn) 
		bmd = datetime.datetime(2001,1,1,0,0,0) 
		realtime = bmd + datetime.timedelta(0,int_dfn) 
		numkey = row[7]
		numkey_pull = ReturnOtherNumber(numkey);
		str_numkey = str(numkey_pull)
	
		message = row[10]
		str_message = str(message)
		messtype = row[14]

		h.write('<tr><td>' + str(realtime) + '</td><td>' + str_numkey + '</td><td>' + str_message + '</td></tr>')

	else:
		time.sleep(0)
h.write('</table>')

h.write('<p><b>Outgoing SMS messages</b></p>')
h.write('<table border="1">')
h.write('<tr><td><b>Date</b></td><td><b>To</b></td><td><b>Message</b></td></tr>')

conn = sqlite3.connect('Burner.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM ZCALLITEM ")
rows = c.fetchall()
for row in rows:

	if row[14] == "outbound_sms":
		rawtime = row[8]
		str_rawtime = str(rawtime)
		dfn = str_rawtime[:9]
		int_dfn = int(dfn) 
		bmd = datetime.datetime(2001,1,1,0,0,0) 
		realtime = bmd + datetime.timedelta(0,int_dfn)
		numkey = row[7]
		numkey_pull = ReturnOtherNumber(numkey);
		str_numkey = str(numkey_pull)
		message = row[10]
		str_message = str(message)
		messtype = row[14]

		h.write('<tr><td>' + str(realtime) + '</td><td>' + str_numkey + '</td><td>' + str_message + '</td></tr>')

	else:
		time.sleep(0)

h.write('</table>')
h.write('<p><b>Outgoing Calls</b></p>')
h.write('<table border="1">')
h.write('<tr><td><b>Date</b></td><td><b>To</b></td></tr>')

conn = sqlite3.connect('Burner.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM ZCALLITEM ") 
rows = c.fetchall()
for row in rows:

	if row[14] == "outbound":
		rawtime = row[8]
		str_rawtime = str(rawtime)
		dfn = str_rawtime[:9] 
		int_dfn = int(dfn) 
		bmd = datetime.datetime(2001,1,1,0,0,0) 
		realtime = bmd + datetime.timedelta(0,int_dfn)
		numkey = row[7]
		numkey_pull = ReturnOtherNumber(numkey);
		str_numkey = str(numkey_pull)
		message = row[10]
		str_message = str(message)
		messtype = row[14]

		h.write('<tr><td>' + str(realtime) + '</td><td>' + str_numkey + '</td></tr>')

	else:
		time.sleep(0)
		
h.write('</table>')
h.write('<p><b>Incoming Calls</b></p>')
h.write('<table border="1">')
h.write('<tr><td><b>Date</b></td><td><b>From</b></td></tr>')
conn = sqlite3.connect('Burner.sqlite')
c=conn.cursor()
c.execute("SELECT * FROM ZCALLITEM ") 
rows = c.fetchall()
for row in rows:

	if row[14] == "call":
		rawtime = row[8]
		str_rawtime = str(rawtime)
		dfn = str_rawtime[:9]
		int_dfn = int(dfn) 
		bmd = datetime.datetime(2001,1,1,0,0,0) 
		realtime = bmd + datetime.timedelta(0,int_dfn) 
		numkey = row[7]
		numkey_pull = ReturnOtherNumber(numkey);
		str_numkey = str(numkey_pull)
		message = row[10]
		str_message = str(message)
		messtype = row[14]
		h.write('<tr><td>' + str(realtime) + '</td><td>' + str_numkey + '</td></tr>')

	else:
		time.sleep(0)
		
h.write('</table>')
h.write("</html>\n")
h.close()
print"[+] Generated HTML file"


