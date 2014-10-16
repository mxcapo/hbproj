import sqlite3
import sys
import csv
from csv import Sniffer
import re

DB = None
CONN = None

def read_csv(csv_table):
	attendees_imm = {}
	f = open(csv_table)
	# f = f.read()
	# maybe = csv.Sniffer()
	# return maybe.has_header(f)
	data = f.read()
	other = data.strip()
	other = data.split(',')

	# new_header = header.split(',')
	# return header
	# new_header = re.split(r'[\r,]', header)
	# return new_header
	# return csv.Sniffer().has_header(new_header)

	# return new_header


	f.close()

	return other



def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect("wedding.db")
	DB = CONN.cursor()	





def main():
	args = sys.argv
	csv_to_read = args[1]
	connect_to_db()

	print read_csv(csv_to_read)




	CONN.close()

if __name__ == "__main__":
	main()