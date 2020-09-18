# coding=utf-8
import os
import jaydebeapi

jarFile = os.path.join(os.path.dirname(os.path.abspath(__file__)),'gsjdbc4.jar')

def connect(user='',password='',dbname='',host='localhost',port=25308):
	url = f'jdbc:postgresql://{host}:{port}/{dbname}'
	driver = 'org.postgresql.Driver'
	conn = jaydebeapi.connect(driver, url, [user, password], jarFile)
	return conn

