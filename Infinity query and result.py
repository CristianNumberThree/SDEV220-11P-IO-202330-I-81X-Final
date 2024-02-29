import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=FRINDBS001;DATABASE=Infinity Proficient;UID=jdillehay_2;PWD=dxk#An8^Y@^G(m3s3wJE8')

cursor = conn.cursor()

sql_query = '''
Select P.F_NAME, T.F_NAME, S.F_USL, S.F_TAR, S.F_LSL
FROM [Infinity Proficient].[dbo].[PART_DAT] as P 
INNER join [Infinity Proficient].[dbo].[SPEC_LIM] as S 
on P.F_NAME = 'MJ-1327 CRC 13mm Inner'
and P.F_PART = S.F_PART 
Inner Join [Infinity Proficient].[dbo].[TEST_DAT] as T
on S.F_TEST = T.F_TEST
'''

cursor.execute(sql_query)

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
conn.close()

###The following is the result of above query.

#Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

#= RESTART: K:\Met_Lab2002\Jen\Python project\Infinity query.py
#('MJ-1327 CRC 13mm Inner', 'Bottom to Ramp', 0.375, 0.37, 0.365)
#('MJ-1327 CRC 13mm Inner', 'E Dimension', 0.469, 0.462, 0.455)
#('MJ-1327 CRC 13mm Inner', 'H Dimension', 0.254, 0.245, 0.236)
#('MJ-1327 CRC 13mm Inner', 'OAH', 0.74, 0.73, 0.72)
#('MJ-1327 CRC 13mm Inner', 'OD', 0.602, 0.597, 0.592)
#('MJ-1327 CRC 13mm Inner', 'T Dimension', 0.541, 0.534, 0.527)

#========== RESTART: K:\Met_Lab2002\Jen\Python project\Qual Plan GUI.py =========
