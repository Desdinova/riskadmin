#!/usr/bin/env python3
#

import mysql.connector
import sys			# to get command line arguments via argv
import getopt			# to parse command line arguments

helptext = "This text should help you do your job"

def cli(argv):
  try:
    options, arguments = getopt.getopt(argv,"hl")
  except getopt.GetoptError:
    print("type riskadmin -h for help")
    sys.exit(2)
  for opt, arg in options:
    if opt == "-h":
      print(helptext)
    elif opt == "-l":
      conn = mysql.connector.connect(user="root", database="asterisk")
      cursor = conn.cursor()
      query = ("select * from user")
      cursor.execute(query)
      for id in cursor:
        print(id)
      cursor.close()
      conn.close()


if __name__ == "__main__":
   cli(sys.argv[1:])


# print("=======")

# argv contains all arguments passed via command line
# print(sys.argv)


