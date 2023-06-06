# import pandas as pd
# import sqlite3

# conn = sqlite3.connect("./satsuite.sqlite", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
# db_df = pd.read_sql_query(
#     sql="SELECT * FROM questionDetails WHERE section='Math'", con=conn)

# db_df.to_csv('database.csv', index=False)



# 
import MySQLdb
import csv

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()

csv_data = csv.reader('database.csv')
for row in csv_data:

    cursor.execute('INSERT INTO questionDetails (item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d)' \
          'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', 
          row)

mydb.commit()
cursor.close()
