#!/usr/bin/env python3
#
# Author: Florian Novy

import mysql.connector
import sys                      # get command line arguments via argv
import getopt                   # parse command line arguments

helptext = "This text should help you do your job"

# make connection to database and execute qstring
def conn_shell(qstring):
  conn = mysql.connector.connect(user="root", database="asterisk")
  cursor = conn.cursor()
  cursor.execute(qstring)
  return cursor.fetchall()			# https://ianhowson.com/blog/a-quick-guide-to-using-mysql-in-python/
  cursor.close()
  conn.close()
  
class Database():
  def listall(argument):			# list all entries in one table
    listquery = ("SELECT * FROM " + argument)
    data = (conn_shell(listquery))
    print("ID \t\tName \t\tnum_intern \t\tnum_extern \t\tTyp \t\tPIN \t\tEmail \t\t\tXMPP")
    for i in data:				# https://snakify.org/lessons/two_dimensional_lists_arrays/
      for elem in i:
        if elem == None or "":
          elem = "LEER"
          print(elem, end="\t\t\t")
        else:
          print(elem, end="\t\t")
      print()

def cli(argv):
  try:
    options, arguments = getopt.getopt(argv,"hl:")              # argv contains all arguments passed via command line
  except getopt.GetoptError:
    print("type riskadmin -h for help")
    sys.exit(2)
  for opt, arg in options:
    if opt == "-h":
      print(helptext)
    elif opt == "-l":
      Database.listall(arg)

if __name__ == "__main__":              # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
   cli(sys.argv[1:])
