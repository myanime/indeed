import sqlite3
conn = sqlite3.connect('my3.db')
c = conn.cursor()
date = [line.rstrip('\n') for line in open('./date')]
print date[0]

my_table = '''
CREATE TABLE date(ID INTEGER PRIMARY KEY,date)
'''
#c.execute(my_table)
c.execute("INSERT INTO date VALUES (NULL,'ryan')")
conn.commit()
conn.close()
