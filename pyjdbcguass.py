# coding=utf-8
import os
import sys
import codecs
import jaydebeapi
from contextlib import contextmanager
import pyguass
import json

@contextmanager
def gscontext(desc):
	host = desc['kwargs'].get('host')
	port = desc['kwargs'].get('port',25308)
	user = desc['kwargs'].get('user')
	password = desc['kwargs'].get('password')
	dbname = desc['kwargs'].get('db')
	conn = pyguass.connect(host=host,
					port=port,
					user=user,
					password=password,
					dbname=dbname)
	cur = conn.cursor()
	yield cur
	cur.close()
	conn.close()

def batchSQL(sqltext):
	desc = {
		"driver":"pyguass",
		"coding":"utf8",
		"dbname":"czbkdw",
		"kwargs":{
			"user":"dbadmin",
			"password":"dbadmin@123",
			"db":"czbkdw",
			"host":"10.1.210.159",
			"port":25308
		}
	}
	sqls = sqltext.split(';')
	with gscontext(desc) as gscur:
		for sql in sqls:
			try:
				gscur.execute(sql)
			except Exception as e:
				print(sql,e)
				sys.exit(1)

def execSQLFile(f):
	with codecs.open(f,'r','utf-8') as fh:
		sqls = fh.read()
		batchSQL(sqls)

if __name__ == '__main__':
	if len(sys.argv)<2:
		print('Usage:\n%s sqlfile ...' % sys.argv[0])
		sys.exit(1)

	for f in sys.argv[1:]:
		execSQLFile(f)
	sys.exit(0)
