import MySQLdb
import string

db = MySQLdb.connect(host="localhost",
                     user="root", passwd="root",
                     db="blog_db")

print(db)
