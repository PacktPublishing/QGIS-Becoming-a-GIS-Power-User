#!/usr/bin/python

# Import the cgi, and system modules
import cgi, sys
# Import the pyspatialite module
from pyspatialite import dbapi2 as sqlite3

# Connect to the DB
conn = sqlite3.connect('C:\\packt\\c6\\data\\prep\\c6b.sqlite')

# Required header that tells the browser how to render the HTML.
print "Content-Type: text/html\n\n"

# Use connection handler as context
with conn:    
    c = conn.cursor()    
    c.execute('SELECT SQLITE_VERSION()')
    
    data = c.fetchone()
    print data
    print 'SQLite version:{0}'.format(data[0])

