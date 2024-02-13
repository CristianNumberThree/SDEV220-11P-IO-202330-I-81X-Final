#Green Team Final
#The purpose of this code snippet is to query the Database that houses
#the tests that are associated with the specific mold and print
#the test names and spec limits.

#This code has been tested at Berry Global and it works.

import pyodbc

 
#Establish connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=FRINDBS001;DATABASE=Infinity Proficient;UID=jdillehay_2;PWD=dxk#An8^Y@^G(m3s3wJE8')

 
#Create cursor
cursor = conn.cursor()

 
#SQL Query
sql_query = '''

Select P.F_NAME, T.F_NAME, S.F_USL, S.F_TAR, S.F_LSL

FROM [Infinity Proficient].[dbo].[PART_DAT] as P

INNER join [Infinity Proficient].[dbo].[SPEC_LIM] as S

on P.F_NAME = '5660a 60cc square'

and P.F_PART = S.F_PART

Inner Join [Infinity Proficient].[dbo].[TEST_DAT] as T

on S.F_TEST = T.F_TEST

'''

 
#Execute query
cursor.execute(sql_query)

 
#Fetch results
results = cursor.fetchall()

 
#Print results
for row in results:

    print(row)

 
#Close cursor and connection
cursor.close()

conn.close()
