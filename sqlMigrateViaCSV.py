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

    #cursor.execute('INSERT INTO questionDetails (item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d) VALUES({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13})'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])) # (:item_id,:section,:prompt,:body,:passage_directions,:passage_attribution,:passage_body,:style,:correct_choice,:rationale,:a,:b,:c,:d)
    cursor.execute("INSERT INTO questionDetails (item_id,section,prompt,body,passage_directions,passage_attribution,passage_body,style,correct_choice,rationale,a,b,c,d) VALUES (:item_id,:section,:prompt,:body,:passage_directions,:passage_attribution,:passage_body,:style,:correct_choice,:rationale,:a,:b,:c,:d)",
                            {'item_id': row[0], 'section': row[1], 'prompt': row[2], 'body': row[3], 'passage_directions': row[4], 'passage_attribution': row[5], 'passage_body': row[6], 'style': row[7],
                             'correct_choice': row[8], 'rationale': row[9], 'a': row[10], 'b': row[11], 'c': row[12], 'd': row[13]})

mydb.commit()
cursor.close()
