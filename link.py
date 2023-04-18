# import cx_Oracle
# connection = cx_Oracle.connect('GROUP4', 'CkVpA3IHJR', cx_Oracle.makedsn(
#     '140.117.69.70', 1521, service_name='ORCLPDB1'))
# cursor = connection.cursor()
import getpass
import oracledb

connection = oracledb.connect(
    user="GROUP4",
    password='CkVpA3IHJR',
    dsn="140.117.69.60/ORCLPDB1")

print("Successfully connected to Oracle Database")
cursor = connection.cursor()

# Create a table

# x = cursor.execute(
#     """
#     select * from table1
# """)

# print(x.rowcoumt)
