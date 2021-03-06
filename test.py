#!/usr/bin/env python3

from orm import *

if __name__ == '__main__':
	import mysql.connector
	class StringField(Field):
		def __init__(self, name, *attrs):
			super().__init__(name, 'varchar(50)', *attrs)

	class IntField(Field):
		def __init__(self, name, *attrs):
			super().__init__(name, 'int', *attrs)

	class User(Model):
		def __init__(self, *, id = '', userName = '', password = ''):
			self['id'] = id
			self['userName'] = userName
			self['password'] = password
		id = IntField('id', 'primary key', 'not null')
		userName = StringField('username', 'not null')
		password = StringField('password', 'not null')

	database = Database(mysql.connector.connect(user = 'root', password = 'root', database = 'main'))
	database.create(
		User()
	)
	database.insert(
		User(id = 0, userName = 'aaa', password = 'aaa'),
		User(id = 1, userName = 'bbb', password = 'bbb')
	)
	users = database.selectAll(User())
	users.sort(key = lambda user: user['id'], reverse = True)
	for i in users:
		print(i)
	database.commit()
	print(database.isTableExist(User()))
	database.drop(User())
	database.close()
