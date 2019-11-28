import pandas as pd
import pyodbc
  
server = 'tcp:YOUR_SQL_SERVER.database.windows.net,1433'
database = 'dnagahsqldw'
driver= 'ODBC Driver 17 for SQL Server'
uid = '<Your_AD_UID>'
pwd = '<YOUR_AD_PWD>'
  
conn_str = f'Driver={driver};Server={server};Database={database};Uid={uid};Pwd={pwd};Authentication=ActiveDirectoryPassword;'

# Please note ActiveDirectoryIntegrated only works with Windows
# conn_str = f'Driver={driver};Server={server};Database={database};Authentication=ActiveDirectoryIntegrated;'
  
conn = pyodbc.connect(conn_str)
print(f'Connected to {driver}/{database}')
