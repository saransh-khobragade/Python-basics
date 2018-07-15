'''
Created on Aug 20, 2015

@author: sandeep.nerella
'''
class Customer:
    def __init__(self):
        self.__cust_id=None
        self.__age=None
        self.__phone=None
        self.__name=None
        self.__pan=None
        self.__gender=None
        self.__password=None
    def get_cust_id(self):
        return self.__cust_id
    
    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone
    
    def get_name(self):
        return self.__name
    
    def get_pan(self):
        return self.__pan
    
    def get_gender(self):
        return self.__gender
    
    def get_password(self):
        return self.__password
    
    def set_cust_id(self,value):
        self.__cust_id=value
    
    def set_age(self,value):
        self.__age=value
    
    def set_phone(self,value):
        self.__phone=value
    
    def set_name(self,value):
        self.__name=value
    
    def set_pan(self,value):
        self.__pan=value
    
    def set_gender(self,value):
        self.__gender=value
    
    def set_password(self,value):
        self.__password=value

