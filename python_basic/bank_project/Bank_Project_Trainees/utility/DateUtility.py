'''
Created on Aug 6, 2015

@author: Deepak_M05
'''
from datetime import date
def get_todays_date():
    return str(date.today().strftime('%d-%m-%Y'))
