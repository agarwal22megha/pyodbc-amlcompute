import logging
import pyodbc

conn_str = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:<YOUR_SERVER_ADDRESS>,1433;Database=<YOUR_DATABASE_NAME>;Uid=<YOUR_DB_SERVER_USERID>;Pwd={YOUR_DB_SERVER_PWD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
# You can find the connection string on your Azure portal under SQLDW resource > Connection Strings 

logging.warn('************************Trying to connect*********************************')
conn = pyodbc.connect(conn_str)
logging.warn('*********************Connection Successful******************************')
