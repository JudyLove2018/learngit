class read_file(object):
	def __init__():
		pass
	# read csv file
	def pandas_method(filepath):
		from pandas import read_csv
		content = read_csv(filepath,usecols=['id']) # usecols定义取列名称,举例
		ids = content.loc[:,'id']
		for id in ids:
			print(id)
		
	def csv_method(filepath):
		import csv
		contents = csv.reader(open(filepath,encoding='utf-8')
		for row in contents:
			print(row)
			
	# read xml configure file
	def loadconf(filepath):
		from encoder import XML2Dict
		with open(filepath, 'r') as f:
			f_doc = f.read()
		info = XML2Dict().parse(f_doc)['configuration']
		res = {}
		for info_i in info['property']:
			key_name = info_i['name'].decode('utf-8')
			res[key_name] = eval(info_i['value'].decode('utf-8'))
		return res
        
