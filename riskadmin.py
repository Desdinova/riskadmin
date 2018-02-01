#!/usr/bin/env python3
#

import mysql.connector
import sys





conn = mysql.connector.connect(user="root", database="asterisk")
cursor = conn.cursor()

query = ("select * from user")

cursor.execute(query)

for id in cursor:
  print(id)
  
cursor.close()
conn.close()

