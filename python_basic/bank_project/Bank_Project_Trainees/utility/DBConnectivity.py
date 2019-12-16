'''
Created on Jul 29, 2015

@author: Deepak_M05
'''
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('T703068/T703068@10.123.79.59:1521/georli04')

def create_cursor(con):
    return cx_Oracle.Cursor(con)

