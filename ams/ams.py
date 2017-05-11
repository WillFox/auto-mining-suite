from core.driver import build_database
import yaml
import os
import urllib.request
import sys

import logging
# create logger
logger = logging.getLogger('ams')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
#logger.debug('debug message')
#logger.info('info message')
#logger.warn('warn message')
#logger.error('error message')
#logger.critical('critical message')



def load_data_yaml():
	logger.debug("Loading Data Yaml from Source")
	data_path=os.environ.get('AMS_DATA_CONFIG')
	if data_path==None:
		data_path=os.path.join('..','data.yaml')
	logger.debug("Loading Data Yaml from {}".format(data_path))
	f=open(data_path,'r')
	data_config=yaml.load(f)
	return data_config

def check_for_data_files(name,path):
	abs_path=os.path.join(path,name)
	is_file=os.path.isdir(abs_path)
	is_data=os.path.isfile(os.path.join(abs_path,name+'.data'))
	is_descrit=os.path.isfile(os.path.join(abs_path,name+'.info'))
	if is_file and is_data and is_descrit:
		pass
	else:
		

def data_retrieve(name=None):
	logger.info("Started ams data retrieve")
	data_config=load_data_yaml()
	#print(data_config)

	data_path=os.environ.get('AMS_DATA_PATH')
	if data_path==None:
		data_path=os.path.join('..','data')
	data_set_keys=[]
	if name!=None:
		#Run through a single analysis

		#print(data_config.get(name,None))
		data_key=data_config.get(name,None)
		if data_key!=None:
			#Data found in data file
			logger.info('Data key [{}] found in data config'.format(name))
			check_for_data_files(name,data_path)
		else:
			#Information for data set not in data file
			logger.error('DATA IS NOT IN DATA CONFIG FILE: [{}] \nEXITING'.format(name))
			sys.exit()
	else:
		#download all data
		logger.info('No data has been specified, retrieving all data in data config file')

		for data_name in data_config.keys():
			#grab data urls
			logger.info("Retrieving:::{}".format(data_name))
			if 'data' in data_config[data_name].keys():
				try:
					urllib.request.urlretrieve(data_config[data_name]['data'])
				except:
					logger.error('COULD NOT REACH {} for [{}]'.format(data_config[data_name]['data'],data_name))
			else:
				logger.warn('DATA KEY [{}] MISSING "data" field'.format(data_name))
			if 'description' in data_config[data_name].keys():
				try:
					urllib.request.urlretrieve(data_config[data_name]['description'])
				except:
					logger.error('COULD NOT REACH {} for [{}]'.format(data_config[data_name]['description'],data_name))
			else:
				logger.warn('DATA KEY [{}] MISSING "description" FIELD'.format(data_name))

			
	return data_set_keys

def supervised_learning(name=None):
	if name!=None:
		#Run through a single analysis
		pass
	else:
		#download all data
		pass

def unsupervised_learning():
	if name!=None:
		#Run through a single analysis
		pass
	else:
		#download all data
		pass

def random_optimization():
	pass

